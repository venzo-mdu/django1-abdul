from django.contrib import admin
from django.urls import path
from .views import (event_view,event_update,event_delete)

urlpatterns = [
    path('',event_view),
    path('update-event/<str:pk>/',event_update),
    path('delete-event/<str:pk>/',event_delete)
]