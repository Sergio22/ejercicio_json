# -*- coding: utf-8 -*-

import json

retuiteados = int(input('numero mínimo de retuits:'))
hastag = input('Que incluyan el hashtag( 0 para incluir todos):')

with open ('mifile.json') as data_file:
	data = json.load(data_file)
		
for tuits in data:

	if(int(tuits['retweet_count'])>= retuiteados):
		if(hastag==0):
			print "Fecha de creación:", tuits['created_at']
			print tuits['text']
			print("Retuiteado ",tuits['retweet_count']," veces")
			print "Favorito " ,tuits['favorite_count'], " veces"
			hastag_array = tuits['entities']['hashtags']
			for h in hastag_array:
				print h['text']
		else:
			hastag_array = tuits['entities']['hashtags']
			for h in hastag_array:
				print(tuits['retweet_count'])
				print tuits['text']
				if(h['text']==hastag):
					print h['text']

