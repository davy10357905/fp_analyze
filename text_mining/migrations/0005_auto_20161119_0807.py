# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_mining', '0004_term_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='created_at',
            field=models.DateTimeField(default='2016-11-01 12:00:00+08:00'),
        ),
    ]
