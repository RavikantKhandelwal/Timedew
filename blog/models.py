from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .formatChecker import ContentTypeRestrictedFileField
from django.template.defaultfilters import slugify
from django.db.models import F
from PIL import Image
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from blog.badwords import badwords
from django_comments_xtd.moderation import moderator, SpamModerator


class TimedewImportant(models.Model):
	about_us = models.TextField()
	created = models.DateTimeField(default=timezone.now)


class Topic(models.Model):
	user = models.ForeignKey(User)
	topic = models.CharField(max_length=200, unique=True)
	total_content = models.BigIntegerField(default=0)
	slug = models.SlugField()
	created = models.DateTimeField(default=timezone.now)

	def clean(self, *args, **kwargs):
		r = self.topic.title()
		e = Topic.objects.filter(topic=r).exists()
		if e:
			raise ValidationError("Topic already Present with name:- " + str(r))
		super(Topic, self).clean(*args, **kwargs)

	def save(self, *args, **kwargs):
		r = self.topic.title()
		self.slug = slugify(r)
		self.topic = r
		return super(Topic, self).save(*args, **kwargs)

	def __str__(self):
		return '%s' % (self.topic)


class YoutubeVideo(models.Model):
	url = models.URLField(max_length=300)
	video_sent_by = models.ForeignKey(User)
	title = models.CharField(max_length=300)
	created = models.DateTimeField(editable=False, default=timezone.now)

	def __str__(self):
		return '%s' % (self.title)


def extra_present_in_content(content, user):
	e = ContentImage.objects.filter(content__id=content, user=user).exists()
	if e:
		return "Image Added"
	else:
		return "Image Absent"


class Content(models.Model):
	user = models.ForeignKey(User)
	topic = models.ForeignKey(Topic, default=None)
	title = models.CharField(max_length=500)
	thought = models.TextField()
	video = models.ForeignKey(YoutubeVideo, on_delete=models.CASCADE, null=True, blank=True)
	# image url wont work we will have to store the image itself
	#image = ContentTypeRestrictedFileField(upload_to=image_upload_in_topic_directory, null=True, blank=True, content_types=['image/jpg', 'image/jpeg', 'image/png', 'image/gif'], max_upload_size=3145728,)
	# this is the url of video like youtube or vimeo
	# video_url = models.URLField(max_length=500, null=True, blank=True)
	# increase it by one each time a different Ip Views it
	views = models.BigIntegerField(default=0)
	slug = models.SlugField()
	allow_comments = models.BooleanField(default=True)
	created = models.DateTimeField()
	modified = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		self.title = self.title.title()
		self.slug = slugify(self.title)
		if not self.id:
			self.created = timezone.now()
			UserProfile.objects.filter(user=self.user).update(total_uploads=F("total_uploads") + 1)
			Topic.objects.filter(id=self.topic.id).update(total_content=F("total_content") + 1)
		return super(Content, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("content_view", args=[self.user.username, self.id, self.slug])

	def __str__(self):
		return '%s,title: %s, topic: %s' % (self.user.username, self.title, self.topic)


class PostCommentModerator(SpamModerator):
	email_notification = True
	removal_suggestion_notification = True

	def moderate(self, comment, content_object, request):
		# Make a dictionary where the keys are the words of the message and
		# the values are their relative position in the message.
		def clean(word):
			ret = word
			if word.startswith('.') or word.startswith(','):
				ret = word[1:]
			if word.endswith('.') or word.endswith(','):
				ret = word[:-1]
			return ret

		lowcase_comment = comment.comment.lower()
		msg = dict([(clean(w), i) for i, w in enumerate(lowcase_comment.split())])
		for badword in badwords:
			if isinstance(badword, str):
				if lowcase_comment.find(badword) > -1:
					return True
			else:
				lastindex = -1
				for subword in badword:
					if subword in msg:
						if lastindex > -1:
							if msg[subword] == (lastindex + 1):
								lastindex = msg[subword]
						else:
							lastindex = msg[subword]
					else:
						break
				if msg.get(badword[-1]) and msg[badword[-1]] == lastindex:
					return True
		return super(PostCommentModerator, self).moderate(comment, content_object, request)


moderator.register(Content, PostCommentModerator)



# when the person visits it for the first time store it in the below ip model and if it is not present than increase
# the above field views by one if it is present than  don't increase above view but increase below count

def content_image_directory(instance, filename):
	# user_id/uploaded_in_topic/album_name/image_in_topic/created/images/filename
	# since here also there is no created in the path so even when saving the new image it will override the previous one
	# try it
	return 'user_%s/image/%s/%s' % (instance.user.username, instance.content.slug, filename)


class ContentImage(models.Model):
	# from post save add this model
	user = models.ForeignKey(User)
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	image = ContentTypeRestrictedFileField(upload_to=content_image_directory, content_types=['image/jpg', 'image/jpeg', 'image/png', 'image/gif'], max_upload_size=3145728, null=True, blank=True)
	other_image = ContentTypeRestrictedFileField(upload_to=content_image_directory, content_types=['image/jpg', 'image/jpeg', 'image/png', 'image/gif'], max_upload_size=3145728, null=True, blank=True)
	other_image_url = models.CharField(max_length=400, null=True, blank=True)
	third_image = ContentTypeRestrictedFileField(upload_to=content_image_directory, content_types=['image/jpg', 'image/jpeg', 'image/png', 'image/gif'], max_upload_size=3145728, null=True, blank=True)
	third_image_url = models.CharField(max_length=400, null=True, blank=True)
	created = models.DateTimeField()
	modified = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		if self.other_image:
			self.other_image_url = self.other_image.url
		if self.third_image:
			self.third_image_url = self.third_image.url
		if not self.id:
			self.created = timezone.now()
		return super(ContentImage, self).save(*args, **kwargs)

	def __str__(self, *args, **kwargs):
		return '%s, title: %s,Content_Id: %s, Image' % (self.user.username, self.content.title, self.content.id)


def user_profile_image(instance, filename):
	# since even when saving the image we don't have created part so new image will be saved at same location
	# overriding previous one
	# try it
	return 'u_id_%s/profile/%s' % (instance.user.username, filename)


class UserProfile(models.Model):
	user = models.ForeignKey(User)
	image = ContentTypeRestrictedFileField(upload_to=user_profile_image,
											content_types=['image/jpg', 'image/jpeg', 'image/png'],
											max_upload_size=3145728, null=True, blank=True)
	total_uploads = models.BigIntegerField(default=0)
	# this is addition of all the views that a person gets combining those from the uploads
	total_views = models.BigIntegerField(default=0)
	description = models.CharField(max_length=100, null=True, blank=True)
	created = models.DateTimeField()
	modified = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		return super(UserProfile, self).save(*args, **kwargs)
