from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'apps.events.views.index', name = "index"),

    url(r'^panel/$', 'apps.events.views.main_panel', name = "panel"),
    url(r'^panel/evento/nuevo/$', 'apps.events.views.crear_evento', name = "nuevo"),
]
