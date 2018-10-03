from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from el_pagination.decorators import page_template, page_templates
from django.contrib.auth.models import User
from operator import attrgetter
from itertools import chain
from django.contrib.auth.decorators import login_required
from .forms import *
from datetime import datetime, timedelta


@page_templates({
	'blog/center_home_page.html': None,
	#'blog/right_home_page.html': 'right_side_list_page',
})
def home_page(request, filter_view=False, extra_context=None, template="blog/home_page.html"):
	# final will be the recent stuff
	# xyz will be the name of users
	if filter_view:
		final = Content.objects.all().order_by("-views")
	else:
		# this means that filter date is true or just home page visit
		final = Content.objects.all().order_by("-created")
	#superusers = User.objects.filter(is_superuser=True).values_list("id", flat=True)
	#xyz = User.objects.order_by("-userprofile__total_views", "-userprofile__total_uploads").exclude(id__in=superusers)
	t = Topic.objects.all().order_by("topic")
	context = {
	"final_content": final,
	"right_side_list": [],
	"topics": t,
	}
	if extra_context is not None:
		context.update(extra_context)
	return render(request, template, context)


@page_templates({
	'blog/center_home_page.html': None,
	#'blog/right_home_page.html': 'right_side_list_page',
})
def topic_page(request, topic_slug, tid=None, filter_view=False, extra_context=None, template="blog/home_page.html"):
	# final will be the recent stuff
	# xyz will be the name of users	
	topic = get_object_or_404(Topic, id=tid, slug=topic_slug)
	if filter_view:
		final = Content.objects.filter(topic=topic).order_by("-views")
	else:
		final = Content.objects.filter(topic=topic).order_by("-created")
	#superusers = User.objects.filter(is_superuser=True).values_list("id", flat=True)
	#xyz = User.objects.order_by("-userprofile__total_views", "-userprofile__total_uploads").exclude(id__in=superusers)
	t = Topic.objects.all().order_by("topic")
	context = {
	"final_content": final,
	"right_side_list": [],
	"topics": t,
	"topic": topic
	}
	if extra_context is not None:
		context.update(extra_context)
	return render(request, template, context)


@page_templates({
	'blog/center_home_page.html': None,
	#'blog/right_home_page.html': 'right_side_list_page',
})
def user_page(request, username, filter_view=False, extra_context=None, template="blog/home_page.html"):
	upload_user = get_object_or_404(UserProfile, user__username=username)
	total_uploads = upload_user.total_uploads
	if filter_view:
		final = Content.objects.filter(user=upload_user.user).order_by("-views")
	else:
		final = Content.objects.filter(user=upload_user.user).order_by("-created")
	#superusers = User.objects.filter(is_superuser=True).values_list("id", flat=True)
	#xyz = User.objects.order_by("-userprofile__total_views", "-userprofile__total_uploads").exclude(id__in=superusers)
	context = {
	"upload_user": upload_user,
	"final_content": final,
	"right_side_list": [],
	"total_uploads": total_uploads
	}
	if extra_context is not None:
		context.update(extra_context)
	return render(request, template, context)


@page_templates({
	#'blog/right_home_page.html': 'right_side_list_page',
})
def content_view(request, username, content_id, page_slug, extra_context=None, template="blog/content.html"):
	# may be possible some unknown user
	upload_user = get_object_or_404(UserProfile, user__username=username)
	total_uploads = upload_user.total_uploads
	content = get_object_or_404(Content, user__username=username, pk=content_id, slug=page_slug)
	to = content.topic
	other_content_by_same_user = Content.objects.filter(user__username=username).exclude(id=content.id)
	vl = other_content_by_same_user.values_list('id', flat=True)
	other_content_by_same_topic = Content.objects.filter(topic=to).exclude(id__in=vl).exclude(id=content.id)
	other_content = sorted(chain(other_content_by_same_topic, other_content_by_same_user), key=attrgetter('views'), reverse=True)
	#ip = get_real_ip(request) <!-- use this when in production
	view_count = content.views
	if not request.user.is_authenticated():
		Content.objects.filter(pk=content.id).update(views=F("views") + 1)
		UserProfile.objects.filter(user=upload_user.user).update(total_views=F('total_views') + 1)
		view_count += 1
	# we don't have an ip address for user
	#superusers = User.objects.filter(is_superuser=True).values_list("id", flat=True)
	# arrange all the timedewers on the basis of all the views they obtained
	#xyz = User.objects.order_by("-userprofile__total_views", "-userprofile__total_uploads").exclude(id__in=superusers)
	context = {
	"content_page": True,
	"final_content": content,
	"view_count": view_count,
	"right_side_list": [],
	"upload_user": upload_user,
	"total_uploads": total_uploads,
	"other_content": other_content[:5],
	}
	if extra_context is not None:
		context.update(extra_context)
	return render(request, template, context)


@login_required
def add_topic(request):
	user = request.user
	form = TopicModelForm(request.POST or None)
	if form.is_valid():
		s = form.save(commit=False)
		s.user = user
		form.save()
		return redirect('upload_new_content')
	context = {
		'user': user,
		'form': form,
	}
	return render(request, 'blog/add_topic.html', context)


@login_required
def upload_new_content(request):
	user = request.user
	content_form = ContentModelForm(request.POST or None)
	image_form = ContentImageModelForm(request.POST or None, request.FILES or None)
	cfv = content_form.is_valid()
	ifv = image_form.is_valid()
	if cfv and ifv:
		a = content_form.save(commit=False)
		a.user = user
		content_instance = content_form.save()
		b = image_form.save(commit=False)
		b.content = content_instance
		b.user = user
		image_form.save()
		return redirect('home_page')
	context = {
		'content_form': content_form,
		'image_form': image_form,
		'user': user,
	}
	return render(request, 'blog/upload_content.html', context)


@login_required
def edit_content(request, content_id):
	user = request.user
	e = get_object_or_404(Content, pk=content_id, user=user)
	i = None
	if ContentImage.objects.filter(content=e, user=user).exists():
		i = get_object_or_404(ContentImage, content=e, user=user)
	content_form = ContentModelForm(request.POST or None, instance=e)
	image_form = ContentImageModelForm(request.POST or None, request.FILES or None, instance=i)
	if content_form.is_valid() and image_form.is_valid():
		a = content_form.save(commit=False)
		a.user = user
		content_instance = content_form.save()
		b = image_form.save(commit=False)
		b.content = content_instance
		b.user = user
		image_form.save()
		return redirect('content_view', username=content_instance.user.username, content_id=content_instance.id, page_slug=content_instance.slug)
		return redirect('home_page')
	context = {
		'content_form': content_form,
		'image_form': image_form,
		'user': user,
	}
	return render(request, 'blog/upload_content.html', context)


@login_required
def edit_profile(request):
	user = request.user
	user_profile_instance = get_object_or_404(UserProfile, user=user)
	user_profile_form = UserProfileModelForm(request.POST or None, request.FILES or None, instance=user_profile_instance)
	user_form = UserFullNameModelForm(request.POST or None, instance=user)
	if user_profile_form.is_valid() and user_form.is_valid():
		user_profile_form.save()
		user_form.save()
		return redirect('user_page', username=user.username)
	context={
		'user_profile_form': user_profile_form,
		'user_form': user_form,
	}
	return render(request, 'blog/edit_profile.html', context)


def about_us(request):
	text = TimedewImportant.objects.latest('created').about_us
	context = {
		'text': text,
	}
	return render(request, 'blog/about_us.html', context)
