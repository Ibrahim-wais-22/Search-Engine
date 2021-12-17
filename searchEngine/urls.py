from django.urls import path 
from . import views
app_name = 'searchEngine'
urlpatterns = [
    path('',views.home , name='home'),
    path('result1', views.result1 , name='result1'),
    path('add', views.add , name='add'),
    path('go', views.go , name='go'),
    path('dashboard', views.dashboard , name='dashboard'),
    
]
