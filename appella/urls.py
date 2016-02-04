from django.conf.urls import url, include
from . import views

urlpatterns = [
    # ex: /ella/
#    url(r'^$', include('django_socketio.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^prueba/$', views.prueba, name='prueba'),
    url(r'^registrar/$', views.registrar, name='registrar'),
    url(r'^perdido/$', views.perdido, name='perdido'),
]
'''
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^insertar/$', views.insertar, name='insertar'),
    url(r'^actualizar/$', views.actualizar, name='actualizar'),
    url(r'^borrar/$', views.borrar, name='borrar'),
    url(r'^ver/$', views.ver, name='ver'),
    url(r'^ejemplo1/$', views.ejemplo1),
    url(r'^ejemplo2/$', views.ejemplo2),
    url(r'^ejemplo3/$', views.ejemplo3),
    url(r'^ejemplo4/$', views.ejemplo4),
'''
