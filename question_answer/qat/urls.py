from django.conf.urls import patterns, include, url

from .views import (HomePageView,
   CardListView, CardDetailView,
   AskListView,AskDetailView,
   AnswerListView, AnswerDetailView)


answer_patterns = patterns(
    '',
    url(r'^d/(?P<pk>\d+)/$', AnswerDetailView.as_view(), name='detail'),
    url(r'^l$', AnswerListView.as_view(), name='list'),
    url(r'^l$', AnswerListView.as_view(), name='create'),
    url(r'^d/(?P<pk>\d+)/$', AnswerDetailView.as_view(), name='update'),
    url(r'^d/(?P<pk>\d+)/$', AnswerDetailView.as_view(), name='delete'),
)


asks_patterns = patterns(
    '',
    url(r'^d/(?P<pk>\d+)/$', AskDetailView.as_view(), name='detail'),
    url(r'^l$', AskListView.as_view(), name='list'),
    url(r'^l$', AskListView.as_view(), name='create'),
    url(r'^d/(?P<pk>\d+)/$', AskDetailView.as_view(), name='update'),
    url(r'^d/(?P<pk>\d+)/$', AskDetailView.as_view(), name='delete'),
)


cards_patterns = patterns(
    '',
    url(r'^d/(?P<pk>\d+)/$', CardDetailView.as_view(), name='detail'),
    url(r'^l$', CardListView.as_view(), name='list'),
    url(r'^l$', CardListView.as_view(), name='create'),
    url(r'^d/(?P<pk>\d+)/$', CardDetailView.as_view(), name='update'),
    url(r'^d/(?P<pk>\d+)/$', CardDetailView.as_view(), name='delete'),
)


urlpatterns = patterns('',
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^answer/', include(answer_patterns, namespace='answer')),
    url(r'^ask/', include(asks_patterns, namespace='ask')),
    url(r'^', include(cards_patterns, namespace='card')),
)
