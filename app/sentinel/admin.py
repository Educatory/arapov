from django.contrib import admin

from app.sentinel.models import BBoxImage, BBox

admin.site.register(BBox)
admin.site.register(BBoxImage)
