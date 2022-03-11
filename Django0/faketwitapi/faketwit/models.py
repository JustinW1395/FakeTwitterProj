from django.db import models


class Tweets(models.Model):
    tweet_text = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('tweet_text',)

    def __str__(self):
        return self.tweet_text