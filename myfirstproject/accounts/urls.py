from django.contrib import admin
from django.urls import path
from .views import (home_view,login_view,logout_view,register_view,profile_view,create_profile,update_profile,changepassword)
# forgotPasswordDone,forgotpassword
urlpatterns = [
    path('',home_view),
    path('login/',login_view),
    path('logout/',logout_view),
    path('register/',register_view),
    path('profile/',profile_view),
    path('create/',create_profile),
    path('update/',update_profile),
    path('changepassword/',changepassword)
]