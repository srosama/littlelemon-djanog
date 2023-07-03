from rest_framework import serializers
from .models import MenuModel, BookingModel
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
     class Meta:
            model = User
            fields = ['url', 'username', 'email', 'groups']