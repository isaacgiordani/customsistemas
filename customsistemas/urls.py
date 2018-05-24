from django.conf.urls import url#, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from django.contrib.auth.views import login

from core import views
from listatelefonica import views as views_listatelefonica

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^telefones/', views_listatelefonica.telefones, name='telefones'),
    url(r'^admin/', admin.site.urls),
]
