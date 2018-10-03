# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-21 06:49
from __future__ import unicode_literals

import blog.formatChecker
import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0017_contentimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.URLField(max_length=500)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Content')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='contentimage',
            name='image',
            field=blog.formatChecker.ContentTypeRestrictedFileField(upload_to=blog.models.content_image_directory),
        ),
    ]
