
from django.urls import path
from . import views


app_name = 'classroom'

urlpatterns = [
    
    path('', views.classroom_list, name='classroom_list'),
    path('classroom/<int:classroom_id>/add_tutorial/', views.add_tutorial, name='add_tutorial'),
    path('tutorial/<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),
    path('classroom/<int:classroom_id>/', views.classroom_detail, name='classroom_detail'),
    path('create/', views.classroom_create, name='classroom_create'),

]
