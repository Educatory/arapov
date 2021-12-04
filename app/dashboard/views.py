from django.views.generic import TemplateView

from app.core.views import DashboardContextMixin
from app.oilpipline.models import OilPipline, Detection
from app.sentinel.models import BBox


class DashboardIndex(DashboardContextMixin):

    template_name = 'dashboard/index.html'
    page_title = 'Информационная доска'

    def get_context_data(self, **kwargs):
        context = super(DashboardIndex, self).get_context_data(**kwargs)
        context.update({
            'boxes': BBox.get_boxes_json(),
            'olis': OilPipline.get_boxes_json(),
            'detects': Detection.to_json()
        })
        return context


class KapotIndex(DashboardIndex):
    template_name = 'dashboard/index.html'
    page_title = 'Под капот'