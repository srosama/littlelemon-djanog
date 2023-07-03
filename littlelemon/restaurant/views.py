from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView , DestroyAPIView 
from rest_framework.viewsets import ModelViewSet
from .serializer import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.decorators import api_view
from .models import MenuModel, BookingModel
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


class MenuItemsView(ListCreateAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
