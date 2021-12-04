from django import template

from app.oilpipline.models import Detection

register = template.Library()


@register.inclusion_tag(
    'olipipline/detections/_notify.html', takes_context=True)
def get_detections_notify(context, count=10):
    detections = Detection.objects.filter(active=True)[:count]
    context['detections'] = detections
    return context

