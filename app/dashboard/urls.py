from django.urls import path

from app.dashboard.views import DashboardIndex

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardIndex.as_view(), name='index'),
]