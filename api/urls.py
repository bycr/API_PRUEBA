from django.urls import include, re_path
from api import views

urlpatterns = [
    re_path(r'^document$', views.DocumentAPi),
    re_path(r'^document/([0-9]+)$', views.DocumentAPi),
    
    re_path(r'^user$', views.UserAPi),
    re_path(r'^user/([0-9]+)$', views.UserAPi)
]