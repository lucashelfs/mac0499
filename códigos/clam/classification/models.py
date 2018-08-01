from django.db import models


class Tweet(models.Model):
    tweet_text = models.TextField(verbose_name='text', max_length=300)
    tweet_username = models.CharField(verbose_name='username', max_length=255)
    tweet_id = models.BigIntegerField(verbose_name='id do tweet')

    def __str__(self):
        return self.tweet_text


class Review(models.Model):
    review = (
        (1, 'Positivo'),
        (0, 'Neutro'),
        (-1, 'Negativo')
    )
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    ironic = models.BooleanField(verbose_name='contem ironia', default=False)
    review = models.IntegerField(verbose_name='Avaliacao', choices=review)

    def is_ironic(self):
        return self.ironic

    def __str__(self):
        return self.tweet.tweet_text
