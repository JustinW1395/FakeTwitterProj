from rest_framework import serializers
from .models import Tweets
from django.contrib.auth.models import User



class TweetSerializer(serializers.HyperlinkedModelSerializer):

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

