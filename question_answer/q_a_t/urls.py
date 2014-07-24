from django.conf.urls import patterns, include, url

from .views import HomePageView, SignUpView, LoginView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'question_answer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', SignUpView.as_view(), name='logout'),
)
