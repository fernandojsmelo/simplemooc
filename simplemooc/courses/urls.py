from django.conf.urls import include, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$',views.index, name='index'),
    #url(r'^(?P<pk>\d+)/$',views.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/$',views.details, name='details'),

]