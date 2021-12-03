from django.contrib import admin

from app.oilpipline.models import OilPipline, Detection


class DetectionAdminInline(admin.StackedInline):
    model = Detection


@admin.register(OilPipline)
class OilPiplineAdmin(admin.ModelAdmin):
    inlines = [DetectionAdminInline]


