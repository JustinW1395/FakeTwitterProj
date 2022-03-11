from rest_framework import serializers
from .models import Tweets
from django.contrib.auth.models import User


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    # We just want to display the owner username (read-only)
    # We want to display the game cagory's name instead of the id

    class Meta:
        model = Tweets
        fields = (
                'tweet_text',
                'date')


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