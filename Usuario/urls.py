from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^Login/$', views.logar, name='logar'),
    url(r'^Cadastrar/$', views.cadastrar, name='cadastrar'),
    url(r'^Sair/$', views.deslogar, name='deslogar'),
    url(r'^Consultar/$', views.consultar, name='consultar'),
    url(r'^Consultar/RelacaoPacoteSoftInstalado/$', views.RelacaoPacoteSoftInstaladoLaboratorio, name='consultarResultado'),
    url(r'^Consultar/PrazoAtendSolicitaReserva/$', views.PrazoAtenReservaLaboratorio, name='prazoSolicitacaoReservaLab'),
    url(r'^Consultar/LabPorData/$', views.LaboratorioReserData, name='consultarLabPorData'),
    url(r'^Consultar/SolicitarSoftware/$', views.solicitarReserva, name='solicitacaoSoftware'),
)