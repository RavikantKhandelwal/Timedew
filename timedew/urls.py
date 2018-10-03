"""timedew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_view
from django.contrib.auth import views as auth_views
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': 'home_page'}, name='logout'),
    url(r'^sec/admin/', admin.site.urls),
    url(r'^upload/content/$', blog_view.upload_new_content, name="upload_new_content"),
    url(r'^e/(?P<content_id>\w+)/content/$', blog_view.edit_content, name="edit_content"),
    url(r'^add/topic/$', blog_view.add_topic, name="add_topic"),
    url(r'^profile/$', blog_view.edit_profile, name="edit_profile"),
    url(r'^$', blog_view.home_page),
    url(r'^home/$', blog_view.home_page, name="home_page"),
    url(r'^h/v/home/$', blog_view.home_page, {'filter_view': True}, name="home_page_filter_view"),
    # we will need to check whether the username and content id matches with the slug
    # because the below url is of three variable so if we take 3  stuff in our url it will automatically direct to this
    url(r'^(?P<username>\w+)/c/(?P<content_id>\w+)/(?P<page_slug>[\w-]+)/$', blog_view.content_view, name="content_view"),
    url(r'^(?P<username>\w+)/$', blog_view.user_page, name="user_page"),
    url(r'^v/(?P<username>\w+)/$', blog_view.user_page, {'filter_view': True}, name="user_page_filter_view"),
    url(r'^(?P<topic_slug>[\w-]+)/t/(?P<tid>\w+)/$', blog_view.topic_page, name="topics_page"),
    url(r'^(?P<topic_slug>[\w-]+)/t/v/(?P<tid>\w+)/$', blog_view.topic_page, {'filter_view': True}, name="topics_page_filter_view"),
    url(r'about/timedew/$', blog_view.about_us, name="about_us"),
    url(r'^comments/', include('django_comments_xtd.urls')),
    url(r'^js/jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
