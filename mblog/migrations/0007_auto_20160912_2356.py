# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mblog', '0006_auto_20160912_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='post date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]