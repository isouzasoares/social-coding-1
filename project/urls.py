from django.conf.urls import patterns, include, url

from django.contrib import admin

from core.views import HomepageView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^login/$', 'core.views.fq_login', name='fq_login'),
    url(r'fq/.*', 'core.views.fq_auth', name='fq_auth'),
    url(r'^admin/', include(admin.site.urls)),
)
