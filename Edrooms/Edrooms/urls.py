
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('classroom/', include('classroom.urls')),
    path('', views.index, name='home'),
    path('', include('user.urls')),
    path('about/', views.about, name='about'),
    

    
    path('admin/', admin.site.urls),
    
]


