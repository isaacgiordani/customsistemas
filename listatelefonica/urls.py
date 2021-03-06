# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.entity_list, name='entity_list'),
    url(r'^contatos/$', views.phone_list, name='phone_list'),
    url(r'^contatos/(?P<slug>[\w_-]+)/$', views.phone, name='phone'),
    url(r'^(?P<slug>[\w_-]+)/$', views.entity, name='entity'),
]
