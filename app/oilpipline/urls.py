from django.urls import path

from app.oilpipline.views import DetectionDetail, OilPiplineDetail, DetectionList, OilPiplineList

app_name = 'oilpipline'

urlpatterns = [
    path('', OilPiplineList.as_view(), name='oli-list'),
    path('<int:pk>/', OilPiplineDetail.as_view(), name='oli'),
    path('detection/<int:pk>/', DetectionDetail.as_view(), name='detection'),
    path('detection/', DetectionList.as_view(), name='detection-list'),

]
