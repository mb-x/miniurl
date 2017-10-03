from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='url_liste'),
    url(r'^new$', views.new, name='url_new'),
     # (?P<code>\w{6}) capturera 6 caractères alphanumériques.
    url(r'^(?P<code>\w{6})/$', views.forword, name='url_forword'),
]