from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from app.core.views import IndexView

urlpatterns = [
    path('accounts/', include('app.account.urls')),
    path('dashboard/', include('app.dashboard.urls', namespace='dashboard')),

    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
