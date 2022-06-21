
from django.urls import path
from App_RegLog import views

app_name = 'App_RegLog'


urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('user_profile/',views.user_profile, name='user_profile'),
    path('other_user_profile/<username>/', views.other_user_profile, name='other_user_profile'),
    path('follow/<username>/', views.follow, name='follow'),
    path('unfollow/<username>/', views.unfollow, name='unfollow'),
    path('post/<pk>/', views.post, name='post')


]
