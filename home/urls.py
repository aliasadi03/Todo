from django.urls import path, include
from . import views
from accounts.views import Login
from .views import forget_password

urlpatterns = [
    path('', Login, name='login'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('task_lists/', views.task_lists, name='task_lists'),
    path('task_list/<int:pk>/', views.task_list_detail, name='task_list_detail'),
    path('task_list/new/', views.task_list_new, name='task_list_new'),
    path('task_list/<int:pk>/edit/', views.task_list_edit, name='task_list_edit'),
    path('task_list/<int:pk>/delete/', views.task_list_delete, name='task_list_delete'),
    path('task_list/<int:pk>/task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('user/<signed_value>/change_password/', views.change_password, name='change_password'),
    path('', views.task_lists, name='index'),
    path('tasks/<int:pk>/', views.task_list_detail, name='tasks'),
]