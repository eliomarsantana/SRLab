from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^Relatorios/$', views.AppRelatorios, name='AppRelatorios'),
    url(r'^Relatorios/ReservaNaoAtendida/$', views.ReservaNaoAtendida, name='ReservaNaoAtendida'),
)