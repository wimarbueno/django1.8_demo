from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'apps.events.views.index'),
]
