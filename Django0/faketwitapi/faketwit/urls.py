from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^tweets/$', views.TweetList.as_view(),
    name=views.TweetList.name),
    re_path(r'^tweets/(?P<pk>[0-9]+)/$', views.tweet_detail),
    re_path(r'^$',views.ApiRoot.as_view(),name=views.ApiRoot.name),
]