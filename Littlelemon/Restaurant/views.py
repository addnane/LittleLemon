from .models import Menu,Booking
from .serializers import MenuSerializer,BookSerializer,UserSerializer
from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView


# Create your views here.


def index(request):
    return render(request, 'index.html', {})


from django.views.generic import ListView
from .models import Menu

class MenuItemView(APIView):
    def get(self, request):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        return Response(serializer.data)
class SingleMenuItemView (generics.RetrieveAPIView):
    queryset =Menu
    serializer_class = MenuSerializer

class BookingViewSet (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]


