import re
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Tweets, Relations
from .serializers import TweetSerializer, UserCreateSerializer, UserSerializer, FollowSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly, IsFollowOrReadOnly


# Create your views here.


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class TweetList(generics.ListCreateAPIView):
    queryset = Tweets.objects.all()
    serializer_class = TweetSerializer
    name = 'tweet-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        # Pass an additional owner field to the create method
        # To Set the owner to the user received in the request
        serializer.save(author=self.request.user)

class FollowList(generics.ListCreateAPIView):
    queryset = Relations.objects.all()
    serializer_class = FollowSerializer
    name = 'relations-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsFollowOrReadOnly)

    def perform_create(self, serializer):
        # Pass an additional owner field to the create method
        # To Set the owner to the user received in the request
        serializer.save(followed=self.request.user)

class FollowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Relations.objects.all()
    serializer_class = FollowSerializer
    name = 'relations-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsFollowOrReadOnly)

class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweets.objects.all()
    serializer_class = TweetSerializer
    name = 'tweets-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny, )
    name = 'user-create'


class UserCreateDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'user-create-detail'

'''@csrf_exempt
def tweet_list(request):
    if request.method == 'GET':
        tweets = Tweets.objects.all()
        tweet_serializer = TweetSerializer(tweets, many=True)
        return JSONResponse(tweet_serializer.data)
    elif request.method == 'POST':
        tweet_data = JSONParser().parse(request)
        tweet_serializer = TweetSerializer(data=tweet_data)
        if tweet_serializer.is_valid():
            tweet_serializer.save()
            return JSONResponse(tweet_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(tweet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

@csrf_exempt
def tweet_detail(request, pk):
    try:
        tweet = Tweets.objects.get(pk=pk)
    except Tweets.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        tweet_serializer = TweetSerializer(tweet)
        return JSONResponse(tweet_serializer.data)
    elif request.method == 'PUT':
        tweet_data = JSONParser().parse(request)
        tweet_serializer = TweetSerializer(tweet, data=tweet_data)
        if tweet_serializer.is_valid():
            tweet_serializer.save()
            return JSONResponse(tweet_serializer.data)
        return JSONResponse(tweet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tweet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'tweets': reverse(TweetList.name, request=request),
            'signup':reverse(UserCreate.name, request=request),
            'users':reverse(UserList.name, request=request),
            'follow':reverse(FollowList.name, request=request)
            })


'''@csrf_exempt
def tweet_list(request):
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        tweet_serializer = TweetSerializer(tweets, many=True)
        return JSONResponse(tweet_serializer.data)
    elif request.method == 'POST':
        tweet_data = JSONParser().parse(request)
        tweet_serializer = TweetSerializer(data=tweet_data)
        if tweet_serializer.is_valid():
            tweet_serializer.save()
            return JSONResponse(tweet_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(tweet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
