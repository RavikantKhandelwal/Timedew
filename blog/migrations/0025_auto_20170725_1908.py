# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-25 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20170725_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
