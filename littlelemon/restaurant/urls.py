from django.urls import path
from .views import *
from rest_framework import routers


urlpatterns = [
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]
