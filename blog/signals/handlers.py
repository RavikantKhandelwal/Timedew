from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import UserProfile, ContentImage
from django.contrib.auth.models import User
from PIL import Image

"""
@receiver(post_save, sender=ContentImage, dispatch_uid="image_manipulation")
def image_resize(sender, instance, created, **kwargs):
	# because creation from admin for user saves the model twice or more times
	if instance.image:
		p = instance.image.path
		# optimization is done now just path finding is remaining
		it = instance.image
		i = Image.open(it)
		i.thumbnail((500, 500), Image.ANTIALIAS)
		i.save(p, optimize=True, quality=75)


@receiver(post_save, sender=UserProfile, dispatch_uid="user_image_manipulation")
def user_image_resize(sender, instance, created, **kwargs):
	# because creation from admin for user saves the model twice or more times
	if instance.image:
		p = instance.image.path
		it = instance.image
		i = Image.open(it)
		i.thumbnail((130, 130), Image.ANTIALIAS)
		i.save(p, optimize=True, quality=65)"""


@receiver(post_save, sender=User, dispatch_uid="user_profile_create")
def user_profile_creation(sender, instance, created, **kwargs):
	# because creation from admin for user saves the model twice or more times
	exist = UserProfile.objects.filter(user=instance).exists()
	if not exist:
		UserProfile.objects.create(user=instance)
