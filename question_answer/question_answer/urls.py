from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import qat

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'question_answer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('qat.urls', namespace='qat',)),
    url(r'^', include('auth.urls', namespace='auth',)),
)
