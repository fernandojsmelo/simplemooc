from django.conf.urls import include, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^tag/(?P<tag>[\w_-]+)/$',views.index, name='index_tagged'),
    ]