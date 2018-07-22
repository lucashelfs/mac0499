import csv
import json
import re
import sys
import time

colunas_clam = ['tweet_id', 'tweet_username', 'tweet_text', 'id']

filename 	= '../dados/presidenciaveis-' + time.strftime("%d-%m-%Y") + '.json'
output 		= '../dados_clam/presidenciaveis-' + time.strftime("%d-%m-%Y") + '.csv' 

with open(output, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(colunas_clam)
    
for line in open(filename, 'r'):
    linha = json.loads(line)

    if not 'limit' in linha and not linha['is_quote_status']:
        
        if linha['truncated']:
            text = linha['extended_tweet']['full_text']

        else:            
            text = linha['text']
            
        # retirando links e evitando quebras de linha no csv
        text = re.sub(r"http\S+", "", text).replace("\n", ", ")

        valores = [linha['id_str'], linha['user'][ 'screen_name'], '"' + text + '"', None]  

        with open(output, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(valores)
