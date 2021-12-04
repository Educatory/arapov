from django.urls import path

from app.dashboard.views import DashboardIndex, KapotIndex

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardIndex.as_view(), name='index'),
    path('/kapot', KapotIndex.as_view(), name='kapot'),
]