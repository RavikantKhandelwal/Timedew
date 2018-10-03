from django import forms
from django.contrib.auth.models import User
from .models import Content, ContentImage, Topic, UserProfile
from django.forms import ModelForm, Textarea, Select, TextInput


class TopicModelForm(ModelForm):
	class Meta:
		model = Topic
		fields = {'topic'}
		widgets = {
			'topic': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
		}


class ContentModelForm(ModelForm):
	class Meta:
		model = Content
		fields = {'topic', "title", "thought", "video", "allow_comments"}
		widgets = {
			'thought': Textarea(attrs={'cols': 40, 'rows': 25, 'class': 'form-control', 'required': 'required'}),
			'topic': Select(attrs={'class': 'form-control', 'required': 'required'}),
			'title': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
			'video': Select(attrs={'class': 'form-control'}),
		}


class ContentImageModelForm(ModelForm):
	class Meta:
		model = ContentImage
		fields = {'image'}


class UserProfileModelForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = {'image', 'description'}
		widgets = {
			'description': Textarea(attrs={'cols': 40, 'rows': 6, 'class': 'form-control'}),
		}


class UserFullNameModelForm(ModelForm):
	class Meta:
		model= User
		fields = {'first_name', 'last_name'}
		widgets = {
			'first_name': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
			'last_name': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
		}
