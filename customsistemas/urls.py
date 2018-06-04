from django.conf.urls import url, include
from django.contrib import admin

from core import views
from listatelefonica import views as views_lt

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^telefones/', include(('listatelefonica.urls','listatelefonica'))),
    url(r'^admin/', admin.site.urls),
]
