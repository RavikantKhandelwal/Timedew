# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-19 10:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_content_allow_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iptrack',
            name='content',
        ),
        migrations.DeleteModel(
            name='IpTrack',
        ),
    ]