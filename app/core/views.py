from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class DashboardContextMixin(TemplateView):

    page_title = ""
    page_icon = "icon-pulse2"

    def get_context_data(self, **kwargs):
        context = super(DashboardContextMixin, self).get_context_data(**kwargs)
        context.update({
            'page_title': self.page_title,
            'page_icon': self.page_icon
        })
        return context
