from django.conf.urls import url
from django.contrib.auth import views as auth_views
from simplemooc.accounts import views


urlpatterns = [
    url(r'^entrar/$', auth_views.login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^cadastre-se/$', views.register, name='register'),

]