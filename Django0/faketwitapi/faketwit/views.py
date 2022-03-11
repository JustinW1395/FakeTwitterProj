from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Tweets
from .serializers import TweetSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

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
