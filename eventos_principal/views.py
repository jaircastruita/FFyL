# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Evento
from slider_principal.models import Slide

# Create your views here.
def home(request):
    slider = Slide.objects.all()
    documents = Evento.objects.all()
    return render(request, 'eventos_principal/home.html', { 'documents': documents,
                                                            'slider': slider})
