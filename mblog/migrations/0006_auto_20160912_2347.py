# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 21:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mblog', '0005_auto_20160912_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='post user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
