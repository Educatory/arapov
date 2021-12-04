import json

from django.db import models
from django.utils.safestring import mark_safe


class OilPipline(models.Model):
    """Модел нефтепроводов с координатами"""
    name = models.CharField("Название", max_length=255, db_index=True)
    description = models.TextField("Описание")
    geo_type = models.CharField("Type", default="Feature", max_length=50)
    geometry = models.JSONField('geometry')
    detection = models.BooleanField("Детекция", default=False)

    class Meta:
        verbose_name = 'Нефтепровод'
        verbose_name_plural = "Нефтепроводы"
        ordering = ['name']

    def __str__(self):
        return self.name

    @classmethod
    def get_boxes_json(cls):
        oils = []
        for obj in cls.objects.all():
            oils.append({
                'features': [{
                    "type": "Feature",
                    "geometry": obj.geometry,
                    "properties": {
                        "name": obj.get_popup(),
                        "detections": obj.is_detections
                    }
                }]
                # 'name': obj.name,
                # 'coords': obj.coords
            })
        return json.dumps(oils)

    def get_popup(self):
        name = f'<h4>{self.name}</h4>{self.description}'
        if self.is_detections:
            name += f'<hr>Обнаружены возможные разливы:<br>{self.get_detections()}'
        return mark_safe(name)

    def get_detections(self):
        detections = ''
        for detect in self.detections.filter(active=True):
            detections += f'<span class="badge mb-1 badge-flat border-{detect.type} text-{detect.type}">{detect.get_type_display()}: <a href="#">Участок: {detect.geometry}</a></span>' \
                          f'<br>'
        return detections

    @property
    def is_detections(self):
        return True if self.detections.filter(active=True) else False


class Detection(models.Model):
    """Детекции на объекте"""
    TYPE_DETECTION = (
        ('warning', 'Предупреждение'),
        ('danger', 'Опасно'),

    )
    type = models.CharField("Тип", choices=TYPE_DETECTION, default='warning', max_length=15)
    oli = models.ForeignKey(OilPipline, related_name='detections', on_delete=models.CASCADE)
    active = models.BooleanField("Актуальный", default=True, db_index=True)
    geometry = models.JSONField('geometry')



