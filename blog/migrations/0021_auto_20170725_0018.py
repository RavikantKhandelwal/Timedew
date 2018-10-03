# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-24 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20170725_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentvideo',
            name='content',
        ),
        migrations.RemoveField(
            model_name='contentvideo',
            name='user',
        ),
        migrations.AddField(
            model_name='youtubevideo',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='url',
            field=models.URLField(),
        ),
        migrations.DeleteModel(
            name='ContentVideo',
        ),
    ]
