# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos_principal', '0002_auto_20170425_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='description',
            field=models.TextField(),
        ),
    ]
