"""
URL configuration for Littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Restaurant.views import BookingViewSet,UserViewSet
router1 = DefaultRouter()
router1.register(r'tables',BookingViewSet)
router2=DefaultRouter()
router2.register(r'users', UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Restaurant.urls')),
    path('restaurant/booking/', include(router1.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('',include(router2.urls)),

]