from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('jokes', views.jokes, name='jokes'),
    path('base', views.base, name='base'),
    path('logout', views.signout, name='logout')
]