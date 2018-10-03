from django import template
from ..models import Content, ContentImage

register = template.Library()


@register.simple_tag
def check_image(user, content):
	e = ContentImage.objects.filter(user=user, content=content).exists()
	if e:
		return ContentImage.objects.get(user=user, content=content).image
	else:
		return False


@register.simple_tag
def check_video(user, content):
	e = Content.objects.get(user=user, id=content.id).video
	if e:
		return Content.objects.get(user=user, id=content.id).video.url
	else:
		return False
