from django.conf.urls import patterns, include, url

from .views import SignUpView, LoginView, LogoutView


urlpatterns = patterns('',
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
)
