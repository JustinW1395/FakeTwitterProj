from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^tweets/$', views.tweet_list),
    re_path(r'^tweets/(?P<pk>[0-9]+)/$', views.tweet_detail),
]