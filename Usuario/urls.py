from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^Login/$', views.logar, name='logar'),
    url(r'^Cadastrar/$', views.cadastrar, name='cadastrar'),
    url(r'^Sair/$', views.deslogar, name='deslogar'),
    url(r'^Consultar/$', views.consultar, name='consultar'),
    url(r'^Consultar/Resultado/$', views.consultarResultado, name='consultarResultado'),
)