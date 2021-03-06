# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 14:11
from __future__ import unicode_literals

import blog.formatChecker
import blog.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=blog.formatChecker.ContentTypeRestrictedFileField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='video_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='views',
            field=models.BigIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='iptrack',
            name='count',
            field=models.BigIntegerField(default=0),
        ),
    ]
