from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import q_a_t

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'question_answer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('q_a_t.urls')),
    url(r'^', include('auth.urls')),
)
