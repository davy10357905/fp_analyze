# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_parser', '0003_auto_20161008_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
