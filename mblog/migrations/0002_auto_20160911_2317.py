# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
