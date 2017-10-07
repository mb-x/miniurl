from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.list, name='url_liste'),
    url(r'^new$', views.new, name='url_new'),
     # (?P<code>\w{6}) capturera 6 caractères alphanumériques.
    url(r'^(?P<code>\w{6})/$', views.forword, name='url_forword'),
    #url(r'^faq$', views.FAQView.as_view())
    url(r'^faq', TemplateView.as_view(template_name='blog/faq.html')),
    
    url(r'^blog$', views.ListArticles.as_view(), name="blog_liste"), 
]