# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos_principal', '0003_auto_20170426_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='document',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]