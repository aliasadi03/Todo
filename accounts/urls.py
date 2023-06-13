from django.urls import path, include
from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    #path('', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
]