from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView

urlpatterns = patterns('website.views',
    url(r'^$', TemplateView.as_view(
        template_name='website/home.html'), name='home'),
)
