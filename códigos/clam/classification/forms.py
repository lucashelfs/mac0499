import logging
from django import forms

logger = logging.getLogger("testlogger")


class ReviewForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.tweet = kwargs.pop('tweet', None)
        self.tweet_text = self.tweet.tweet_text
        super(ReviewForm, self).__init__(*args, **kwargs)

    review_choices = (
        (1, 'Positivo'),
        (0, 'Neutro'),
        (-1, 'Negativo')
    )
    review = forms.ChoiceField(choices=review_choices, required=True, label='Opinião do tweet',
                               widget=forms.RadioSelect())
    """
        TODO: when is non related, add option to remove field
    """
    ironic = forms.BooleanField(required=False, label='É irônico / não relacionado?',
                                widget=forms.CheckboxInput(attrs={'class': 'checkbox-inline'}))
    tweet = forms.IntegerField(label='Tweet', widget=forms.HiddenInput())


class ReviewFormSet(forms.BaseFormSet):

    def __init__(self, *args, **kwargs):
        self.tweets = kwargs.pop('tweets', None)
        super(ReviewFormSet, self).__init__(*args, **kwargs)

    def _construct_form(self, i, **kwargs):
        return super(ReviewFormSet, self)._construct_form(
            i, tweet=self.tweets[i], **kwargs)

    def clean(self):
        if any(self.errors):
            return


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Arquivo csv (atenção, os elementos devem ser separados por virgula)')
