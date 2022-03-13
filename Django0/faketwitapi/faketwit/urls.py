from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^tweets/$', views.tweet_list),
    re_path(r'^tweets/(?P<pk>[0-9]+)/$', views.tweet_detail),
     re_path(r'^account/register/$', views.UserCreate.as_view(),name=views.UserCreate.name),
    re_path(r'^account/register/(?P<pk>[0-9]+)/$', views.UserCreateDetail.as_view(),name=views.UserCreateDetail.name),
    re_path(r'^$',views.ApiRoot.as_view(),name=views.ApiRoot.name),
]