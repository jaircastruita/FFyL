# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos_principal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='published_date',
        ),
    ]