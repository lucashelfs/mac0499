import tweepy
import json
import time

# Dados do app no twitter
from consumer_secret import *


class CollectorListener(tweepy.StreamListener):

	filename = './dados/presidenciaveis-' + time.strftime("%d-%m-%Y") + '.json'

	def on_data(self, data):
		
		# imprimir o tweet
		# tweet = json.loads(data)
		# print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))

		# salva os jsons que representam os tweets
		with open(self.filename, 'a') as f:
			f.write(data)

		def on_error(self, status):
			print('Erro! Código: ', status)

		def abre_coletados():
			# Para abrir os tweets que foram salvos pelo listener
			tweets = []
			for line in open('tweets_baixados.json', 'r'):
				tweets.append(json.loads(line))
				return tweets

if __name__ == '__main__':

	listener = CollectorListener()
	print('Coletando tweets contendo os candidatos a presidência...')

	# Autentica
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	# Connecta na API
	stream = tweepy.Stream(auth, listener)
	stream.filter(track=['Lula', 'Bolsonaro', 'Marina Silva', 'Ciro Gomes'])
