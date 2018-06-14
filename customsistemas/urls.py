from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

from core import views
from listatelefonica import views as views_lt

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    #url(r'^registro/$', views.register, name='register'),
    url(r'^lista/', include(('listatelefonica.urls','listatelefonica'))),
    url(r'^admin/', admin.site.urls),
]
