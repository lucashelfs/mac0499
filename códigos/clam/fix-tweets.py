import json
import csv

colunas_clam = ['tweet_id', 'tweet_username', 'tweet_text', 'id']
with open('temer.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(colunas_clam)

for line in open('tweets_temer.json', 'r'):
    linha = json.loads(line)
    if not 'limit' in linha:
        valores = [linha['id_str'], linha['user'][ 'screen_name'], '"'+linha['text']+'"', None]

        with open('temer.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(valores)
