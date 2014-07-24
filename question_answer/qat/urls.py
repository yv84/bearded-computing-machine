from django.conf.urls import patterns, include, url

from .views import HomePageView, CardDetailView, CardListView

urlpatterns = patterns('',
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^d/(?P<pk>\d+)/$', CardDetailView.as_view(), name='detail'),
    url(r'^l$', CardListView.as_view(), name='list'),
    url(r'^l$', CardListView.as_view(), name='create'),
    url(r'^d/(?P<pk>\d+)/$', CardListView.as_view(), name='update'),
    url(r'^d/(?P<pk>\d+)/$', CardListView.as_view(), name='delete'),
)
