# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_content_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='topic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Topic'),
        ),
    ]