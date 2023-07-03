from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView , DestroyAPIView 
from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializer import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.decorators import api_view
from .models import MenuModel, BookingModel
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer



@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
     return Response({"message":"This view is protected"})



class MenuItemsView(ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuModel.objects.all()
  serializer_class = MenuSerializer



