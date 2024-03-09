from django.shortcuts import render
from app.views import *
from app.Serializers import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class productcurd(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
