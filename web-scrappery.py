#!/usr/bin/python

import urllib
from bs4 import BeautifulSoup as BS
# Below file "list" contains list of URL in each line, see example file "list" in https://github.com/krokite/python-web-data-scrapper
fo = open("list", 'r');


print '''

 /$$   /$$                     /$$   /$$ /$$   /$$              
| $$  /$$/                    | $$  /$$/|__/  | $$              
| $$ /$$/   /$$$$$$   /$$$$$$ | $$ /$$/  /$$ /$$$$$$    /$$$$$$ 
| $$$$$/   /$$__  $$ /$$__  $$| $$$$$/  | $$|_  $$_/   /$$__  $$
| $$  $$  | $$  \__/| $$  \ $$| $$  $$  | $$  | $$    | $$$$$$$$
| $$\  $$ | $$      | $$  | $$| $$\  $$ | $$  | $$ /$$| $$_____/
| $$ \  $$| $$      |  $$$$$$/| $$ \  $$| $$  |  $$$$/|  $$$$$$$
|__/  \__/|__/       \______/ |__/  \__/|__/   \___/   \_______/
		'''


for lines in fo:
	line = lines.split('\n')
	html = urllib.urlopen(line[0]).read()
	soup = BS(html, "htmllib")
	try :
		print soup.find(id='mail_id').get_text()
	except AttributeError:
		print "mail_id id Not Available"
