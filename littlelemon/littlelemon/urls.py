from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, BaseRouter
from restaurant import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tables', viewset=views.BookingViewSet , basename='booking')
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    
]
