from django.conf.urls import url

from . import views

app_name = 'classification'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'review/$', views.review, name='review_tweets'),
    url(r'reviewed/$', views.all_reviewed, name='all-reviewed'),
    url(r'^export/csv/$', views.generate_csv, name='generate_csv'),
]
