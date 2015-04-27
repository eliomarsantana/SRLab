from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SRLab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^Administrativo/', include('Administrativo.urls')),
    url(r'^Usuario/', include('Usuario.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Relatorios/', include('Relatorios.urls')),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


