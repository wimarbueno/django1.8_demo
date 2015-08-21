from django.conf.urls import include, url


urlpatterns = [
    url(r'^login/$', 'apps.users.views.userlogin', name = "login"),
    url(r'^logout/$', 'apps.users.views.LogOut', name = "logout"),
]
