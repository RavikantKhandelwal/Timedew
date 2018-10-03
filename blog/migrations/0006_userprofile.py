# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 17:33
from __future__ import unicode_literals

import blog.formatChecker
import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20170717_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', blog.formatChecker.ContentTypeRestrictedFileField(blank=True, null=True, upload_to=blog.models.user_profile_image)),
                ('total_uploads', models.BigIntegerField(default=0)),
                ('created', models.DateTimeField(editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]