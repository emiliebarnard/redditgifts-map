""" 
redditgifts exchange scraper for redditgifts map
emilie barnard


beautiful soup: http://www.crummy.com/software/BeautifulSoup/
"""

import urllib2
from bs4 import BeautifulSoup

#as of 4/7 there are only three pages of exchanges
soup1 = BeautifulSoup(urllib2.urlopen('http://redditgifts.com/exchanges').read())

soup2 = BeautifulSoup(urllib2.urlopen('http://redditgifts.com/exchanges/?page=2').read())

soup3 = BeautifulSoup(urllib2.urlopen('http://redditgifts.com/exchanges/?page=3').read())


exchangeLinks1 = soup1.findAll("a", {"class": "exchangelink"})
exchangeLinks1 = exchangeLinks1[::-1] #reverses the list so most recent is last

exchangeLinks2 = soup2.findAll("a", {"class": "exchangelink"})
exchangeLinks2 = exchangeLinks2[::-1]

exchangeLinks3 = soup3.findAll("a", {"class": "exchangelink"})
exchangeLinks3 = exchangeLinks3[::-1]

allExchangeLinks = exchangeLinks3 + exchangeLinks2 + exchangeLinks1

exchangeNames = [] #this will store the name of all exchanges

for linkElement in allExchangeLinks:
	# elementExchangeName = str(linkElement).replace("</a>", "")
	# for 
	elementExchangeName = str(linkElement.getText())
	exchangeNames.append(elementExchangeName)

##############################################################################
#####this will print the code needed to make the drop-down exchanges box in js

##for the dropbox, we'll display the most recent first, so we reverse the list again
exchangeNamesByRecent = exchangeNames[::-1]

for name in exchangeNamesByRecent:
	print "<option>" + name + "</option>"

