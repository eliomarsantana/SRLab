from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SRLab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^Administrativo/', include('Administrativo.urls')),
    url(r'^Usuario/', include('Usuario.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


