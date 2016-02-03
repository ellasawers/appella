from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registrar/$', views.registrar, name='registrar'),
]
