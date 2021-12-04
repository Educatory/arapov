from django.views.generic import DetailView, ListView

from app.oilpipline.models import Detection, OilPipline


class DetectionDetail(DetailView):
    model = Detection
    template_name = 'olipipline/detections/detail.html'

    @property
    def page_title(self):
        return f'Детекция: на {self.object.oli}'



class DetectionList(ListView):
    model = Detection
    template_name = 'olipipline/detections/list.html'
    page_title = 'Все уведомления'

