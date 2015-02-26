# -*- coding: utf-8 -*-

import json


with open ('mifile.json') as data_file:
	data = json.load(data_file)

for tuits in data:
	print tuits['created_at']	
