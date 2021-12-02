from django.contrib import admin
from django.urls import path, include

from app.core.views import IndexView

urlpatterns = [
    path('accounts/', include('app.account.urls')),
    path('dashboard/', include('app.dashboard.urls', namespace='dashboard')),

    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]
