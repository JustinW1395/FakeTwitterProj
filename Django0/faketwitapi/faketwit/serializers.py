from rest_framework import serializers
from .models import Tweets, Relations
from django.contrib.auth.models import User


class UserTweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweets
        fields = (
            'url',
            'tweet_text')

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

class TweetSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Tweets
        fields = (
                'url',
                'author',
                'tweet_text',
                'date')


class GETFollowTweetSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Tweets
        fields = (
                'url',
                'author',
                'tweet_text',
                'date')
        


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


'''class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    tweet_text = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return Tweets.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tweet_text = validated_data.get('tweet_text', instance.tweet_text)'''


'''class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=200, required=True)
    password = serializers.CharField(max_length=200, required=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)'''