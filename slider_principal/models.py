# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Slide(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200, )
    descripcion = models.TextField()
    documento = models.FileField(upload_to='documents/')
    imagen = models.ImageField(upload_to='documents/slider')
    subido_el = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo