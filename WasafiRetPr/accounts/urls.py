from django.urls import path

from .import views 
app_name='auth'
urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('profile',views.user_profile, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/security/', views.security_settings_view, name='security_settings'),
    

]
