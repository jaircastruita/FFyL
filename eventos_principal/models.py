# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone

class Evento(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, )

    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)
    place = models.CharField(max_length=200)
    description = models.TextField()
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def __str__(self):
        return self.title