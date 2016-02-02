from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^registrar/$', views.registrar, name='registrar'),
]
