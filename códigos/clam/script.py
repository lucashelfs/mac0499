#  Use para importar dados pelo shell

from classification.models import Tweet
import csv
import os

files = []
for filename in os.listdir('data'):
    files.append('data/'+filename)

for file in files:
    with open(file, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            try:
                tweet_id = int(row['id'])
            except ValueError:
                tweet_id = 00000000
            tweet = Tweet(tweet_id=tweet_id, tweet_username=row['tweet_username'], tweet_text=row['tweet_text'])
            tweet.save()
