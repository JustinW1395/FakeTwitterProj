from rest_framework import serializers
from .models import Tweets
from django.contrib.auth.models import User
from .models import Tweets, Relations



class TweetSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Tweets
        fields = (
                'url',
                'author',
                'tweet_text',
                'date')

class UserTweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweets
        fields = (
            'url',
            'tweet_text')

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class FollowSerializer(serializers.HyperlinkedModelSerializer):

    follower = serializers.ReadOnlyField(source='follower.username')

    followed = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Relations
        fields = (
                'url',
                'follower',
                'followed')

class UserFollowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relations
        fields = (
                'url',
                'followed')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tweets = UserTweetSerializer(many=True, read_only=True)
    follow = UserFollowSerializer (many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'url', 
            'pk',
            'username',
            'tweets',
            'follow')

class GETFollowTweetSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Tweets
        fields = (
                'url',
                'author',
                'tweet_text',
                'date')

