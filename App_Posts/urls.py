from django.urls import path
from App_Posts import views

app_name = 'App_Posts'


urlpatterns = [
    path('', views.home, name='home'),
    path('like/<pk>/', views.like, name='like'),
    path('unlike/<pk>/', views.unlike, name='unlike'),





]
