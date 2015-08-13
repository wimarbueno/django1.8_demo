from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = "index"),

    #url(r'^login/$', 'apps.events.views.login', name = "login"),

    url(r'^panel/$', views.MainPanelView.as_view(), name = "panel"),
    url(r'^panel/evento/nuevo/$', views.CreateEvent.as_view(), name = "nuevo"),
    url(r'^panel/evento/(?P<pk>\d+)/$', views.EventDetail.as_view(), name = "detalle"),
    url(r'^panel/editar/(?P<pk>\d+)/$', views.EventEdit.as_view(), name = "editar"),
    url(r'^panel/eliminar/(?P<pk>\d+)/$', views.EventDelete.as_view(), name = "eliminar"),
]
