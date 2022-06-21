from django.shortcuts import render
from rest_framework import viewsets, permissions
from tecban.models import Terminal


from tecban.serializers import TerminalSerializer

class TerminalViewSet(viewsets.ModelViewSet):
  queryset = Terminal.objects.all()
  serializer_class = TerminalSerializer