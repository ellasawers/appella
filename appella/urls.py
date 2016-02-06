from django.conf.urls import url, include
from . import views

urlpatterns = [
    # ex: /ella/
#    url(r'^$', include('django_socketio.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^encontrado/$', views.encontrado, name='encontrado'),
    url(r'^listaencontrados/$', views.listaencontrados),
    url(r'^perdido/$', views.perdido, name='perdido'),
    url(r'^listaperdidos/$', views.listaperdidos),
    url(r'^prueba/$', views.prueba, name='prueba'),
    url(r'^registrar/$', views.registrar, name='registrar'),
    url(r'^mapa/$', views.mapa),
]
