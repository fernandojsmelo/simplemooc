from django.conf.urls import include, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', views.index, name='index_tagged'),
    url( r'^resposta/(?P<pk>[\w_-]+)/correta/$', views.reply_correct, name='reply_correct' ),
    url( r'^resposta/(?P<pk>[\w_-]+)/incorreta/$',views.reply_incorrect,name='inreply_correct' ),
    url(r'^(?P<slug>[\w_-]+)/$', views.thread, name='thread'),
    ]