# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161014_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='intro',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]