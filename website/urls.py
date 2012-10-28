from django.conf.urls import patterns, url, include

urlpatterns = patterns('website.views',
    url(r'^$', 'home', name='home'),
)
