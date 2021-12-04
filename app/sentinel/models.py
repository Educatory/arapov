import json

from django.db import models
from django_extensions.db.models import TimeStampedModel


class BBox(TimeStampedModel):
    max_x = models.FloatField()
    max_y = models.FloatField()
    min_x = models.FloatField()
    min_y = models.FloatField()

    class Meta:
        verbose_name = 'BBOX'
        verbose_name_plural = 'BBOX'

    def lower_left(self):
        return [self.max_y, self.max_x]

    def upper_right(self):
        return [self.min_y, self.min_x]

    @classmethod
    def get_boxes_json(cls):
        boxes = []
        for obj in cls.objects.all():
            boxes.append({
                'imageUrl': obj.bboximage_set.all()[0].image.url,
                'imageBounds': [obj.lower_left(), obj.upper_right()]
            })
        return json.dumps(boxes)


class BBoxImage(TimeStampedModel):
    bbox = models.ForeignKey('sentinel.BBox', verbose_name='BBox', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bbox_img', null=True, blank=True)

    class Meta:
        verbose_name = 'Изображения BBOX'
        verbose_name_plural = 'Изображения BBOX'
        ordering = ['-created']

