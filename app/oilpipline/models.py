import json

from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_extensions.db.models import TimeStampedModel


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
            detections += f'<span class="badge mb-1 badge-flat border-{detect.type} text-{detect.type}">{detect.get_type_display()}: <a href="{detect.get_absolut_url()}">Участок: {detect.geometry}</a></span>' \
                          f'<br>'
        return detections

    @property
    def is_detections(self):
        return True if self.detections.filter(active=True) else False


class Detection(TimeStampedModel):
    """Детекции на объекте"""
    TYPE_DETECTION = (
        ('warning', 'Предупреждение'),
        ('danger', 'Опасно'),
        ('success', 'Успешное обновление'),
        ('info', 'Запрошены данные'),

    )
    type = models.CharField("Тип", choices=TYPE_DETECTION, default='warning', max_length=15)
    oli = models.ForeignKey(OilPipline, related_name='detections', on_delete=models.CASCADE)
    active = models.BooleanField("Актуальный", default=True, db_index=True)
    geometry = models.JSONField('geometry')

    class Meta:
        verbose_name = 'Детекция'
        verbose_name_plural = "Детекции обнаружения"
        ordering = ['-created']

    def get_absolut_url(self):
        return reverse('oilpipline:detection', args=[self.pk])

    @staticmethod
    def to_json():
        lst = []
        for item in Detection.objects.filter(active=True):
            lst.append({
                'coords': item.geometry
            })
        return lst





