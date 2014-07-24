from django.conf.urls import patterns, include, url

from .views import HomePageView

urlpatterns = patterns('',
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^$', HomePageView.as_view(), name='home'),
)
