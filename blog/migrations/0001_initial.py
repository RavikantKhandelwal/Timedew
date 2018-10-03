# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 14:06
from __future__ import unicode_literals

import blog.formatChecker
import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('thought', models.TextField()),
                ('image', blog.formatChecker.ContentTypeRestrictedFileField()),
                ('video_url', models.URLField(max_length=500)),
                ('views', models.BigIntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IpTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('count', models.BigIntegerField()),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Content')),
            ],
        ),
    ]