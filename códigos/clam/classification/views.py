import csv
import logging
import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import formset_factory
from .models import Tweet, Review
from .forms import ReviewForm, ReviewFormSet, CSVUploadForm


def index(request):
    return render(request, 'classification/index.html', None)


def get_n_random(n):
    items = []
    tweets = Tweet.objects.filter(review__isnull=True)
    for i in range(n):
        items.append(random.choice(tweets))
    return items


def review(request):

    formset = formset_factory(ReviewForm, formset=ReviewFormSet, extra=0)
    logger = logging.getLogger('testlogger')

    if request.method == 'POST':
        """
            TODO: fazer query menor para quando for POST, depende do int do else
        """

        tweets = Tweet.objects.filter(review__isnull=True)
        review_formset = formset(request.POST, tweets=tweets)

        if review_formset.is_valid():
            logger.info('vou começar a registrar as opinioes')

            for review_form in review_formset:
                tweet_id = review_form.cleaned_data.get('tweet')
                review = review_form.cleaned_data.get('review')
                ironic = review_form.cleaned_data.get('ironic')
                reviewed_tweet = Tweet.objects.get(pk=tweet_id)
                user_review = Review(
                    tweet=reviewed_tweet,
                    review=review,
                    ironic=ironic
                )
                user_review.save()

            logger.info('terminei de colocar as opinioes')
            return redirect('classification:all-reviewed')

        else:
            context = {'review_formset': review_formset}
            return render(request, 'classification/review.html', context)

    else:
        tweets_amount = int(request.GET['tweets_amount'])
        tweets_to_review = get_n_random(tweets_amount)
        review_formset = formset(initial=[{'tweet': tweet.pk} for tweet in tweets_to_review],
                                 tweets=tweets_to_review)
        context = {'review_formset': review_formset, 'amount': tweets_amount}
        return render(request, 'classification/review.html', context)


def all_reviewed(request):
    reviewed_tweets = Tweet.objects.filter(review__isnull=False)
    context = {'reviewed_tweets': reviewed_tweets}
    return render(request, 'classification/show_reviewed.html', context)


def generate_csv(request):
    """
        TODO: refatorar esse metodo para tirar o if do for, fazer isso antes de deployar pra valer
    """
    logger = logging.getLogger('testlogger')
    logger.info("gerando csv")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tweets_classificados.csv"'
    writer = csv.writer(response)
    writer.writerow(['username', 'tweet', 'review'])
    reviewed_tweets = Tweet.objects.filter(review__isnull=False) \
        .filter(review__ironic=False)

    for tweet in reviewed_tweets:
        logger.info("texto: {}".format(tweet.tweet_text.encode('utf-8').decode('utf-8')))
        writer.writerow(
            [tweet.tweet_username, tweet.tweet_text.encode('utf-8').decode('utf-8'), tweet.review_set.all()[0].review])

    logger.info("csv gerado!")
    return response
