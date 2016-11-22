#!/usr/bin/python

import os
import shutil
import sys
import urllib
import json
import re
import wget

folder2save = "Q:\movies\\"

for x in os.listdir("./"):
	print x
	y = re.match(r"(.*)\.mkv", str(x))
	if y:
		t = y.group(1)
		url='http://www.omdbapi.com/?t='+str(t)
		# moviename='Q:\\'+ t
		response = urllib.urlopen(url).read()
		jsonvalues = json.loads(response)
		print jsonvalues
		if jsonvalues["Response"]=="True":
				imdbrating = jsonvalues['imdbRating']
				print imdbrating+" "+x
				destinationDir = folder2save + jsonvalues['Title']
				print destinationDir
				if not os.path.exists(destinationDir): 
					os.makedirs(destinationDir)
				imurl = jsonvalues['Poster']
				poster = wget.download(imurl)
				shutil.move(poster, destinationDir)
				shutil.move(x, destinationDir)