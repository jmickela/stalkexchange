"""stalkexchange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url("^$", 'userprofile.views.home', name="home"),
    url("^profile/create$", 'userprofile.views.profile_create', name='profile_create'),
    url("^profile/edit", 'userprofile.views.profile_edit', name='profile_edit'),
    url("^profile/(?P<user_id>[0-9]+)", 'userprofile.views.profile_view', name='profile_view'),

    url("^garden/add$", 'produce.views.add_produce_to_profile', name="add_to_garden"),
    url('^garden/(?P<item_id>[0-9]+)/remove', 'produce.views.remove_produce_from_profile', name='remove_from_garden'),

    url('^wishlist/add', 'wishlist.views.wishlist_add_item', name='wishlist_add_item'),
    url('^wishlist/(?P<item_id>[0-9]+)/remove', 'wishlist.views.remove_wishlist_item', name='wishlist_remove_item'),

    url('^search$', 'produce.views.garden_item_search', name='garden_search'),

    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^wiki/', include('waliki.urls')),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
