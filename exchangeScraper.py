""" 
redditgifts exchange scraper for redditgifts map
emilie barnard


beautiful soup: http://www.crummy.com/software/BeautifulSoup/
"""

import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://redditgifts.com/exchanges/?page=3').read())

print (soup.prettify())


