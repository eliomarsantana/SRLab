from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.AppRelatorios, name='AppRelatorios'),
    url(r'^ReservasNaoAtendida/$', views.ReservaNaoAtendida, name='ReservaNaoAtendida'),
    url(r'^Login/$', views.logar, name='logar'),
)