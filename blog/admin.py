from django.contrib import admin
from django import forms
from .models import *


class TimedewImportantModelAdmin(admin.ModelAdmin):
	list_display = ["about_us", "created"]

	class Meta:
		model = TimedewImportant


admin.site.register(TimedewImportant, TimedewImportantModelAdmin)


class TopicModelAdmin(admin.ModelAdmin):
	list_display = ["topic", "slug", "user", "total_content", "created"]

	class Meta:
		model = Topic


admin.site.register(Topic, TopicModelAdmin)


class ContentModelAdmin(admin.ModelAdmin):
	list_display = ["user", "id", "thought", "video", "allow_comments", "topic", "views", "created"]

	class Meta:
		model = Content


admin.site.register(Content, ContentModelAdmin)


class ContentImageModelAdmin(admin.ModelAdmin):
	list_display = ["user", "id", "content", "image", "other_image", "other_image_url", "third_image", "third_image_url", "created"]

	class Meta:
		model = ContentImage

admin.site.register(ContentImage, ContentImageModelAdmin)


class UserProfileModelAdmin(admin.ModelAdmin):
	list_display = ["user", "id", "image", "total_uploads", "total_views", "created"]

	class Meta:
		model = UserProfile


admin.site.register(UserProfile, UserProfileModelAdmin)