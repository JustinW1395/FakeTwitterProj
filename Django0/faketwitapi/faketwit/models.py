from django.db import models
from django.contrib.auth.models import User


class Tweets(models.Model):
    author = models.ForeignKey(  
        'auth.User',            
        related_name='tweets',
        on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('tweet_text',)

    def __str__(self):
        return self.tweet_text

class Relations(models.Model):
    follower = models.ForeignKey(  
        'auth.User',            
        related_name='relations',
        on_delete=models.CASCADE)
    followed = models.ForeignKey(  
        'auth.User',            
        related_name='followed',
        on_delete=models.CASCADE)

    class Meta:
        ordering = ('followed',)