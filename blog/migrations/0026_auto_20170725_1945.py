# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-25 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20170725_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
    ]
