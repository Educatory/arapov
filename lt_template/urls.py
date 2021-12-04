from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app.core.views import IndexView

urlpatterns = [
                  path('accounts/', include('app.account.urls')),
                  path('dashboard/', include('app.dashboard.urls', namespace='dashboard')),
                  url('^inbox/notifications/', include('notifications.urls', namespace='notifications')),
                  path('', IndexView.as_view(), name='index'),
                  path('oli/', include('app.oilpipline.urls', namespace='oil')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
