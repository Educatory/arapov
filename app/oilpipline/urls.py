from django.urls import path, include

from app.oilpipline.views import DetectionDetail

app_name = 'oilpipline'

urlpatterns = [
    path('detection/<int:pk>/', DetectionDetail.as_view(), name='detection'),

]
