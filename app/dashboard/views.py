from django.views.generic import TemplateView

from app.core.views import DashboardContextMixin


class DashboardIndex(DashboardContextMixin):

    template_name = 'dashboard/index.html'
    page_title = 'Информационная доска'
