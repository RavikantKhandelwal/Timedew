# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170717_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='slug',
            field=models.SlugField(default='t', editable=False),
        ),
    ]