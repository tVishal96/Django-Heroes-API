from django.shortcuts import render
from .models import Hero
from rest_framework import viewsets
from .serializers import HeroSerializer


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer