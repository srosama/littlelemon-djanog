from django.contrib import admin
from .models import BookingModel, MenuModel
#Import Model to admin site

admin.site.register(BookingModel)
admin.site.register(MenuModel)