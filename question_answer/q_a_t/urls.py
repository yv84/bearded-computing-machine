from django.conf.urls import patterns, include, url

from .views import HomePageView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'question_answer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home$', HomePageView.as_view(), name='home')
)
