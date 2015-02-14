""" 
redditgifts exchange scraper for redditgifts map
emilie barnard


beautiful soup: http://www.crummy.com/software/BeautifulSoup/
"""
##############################################################################
#### comment and uncomment code printed as needed
##############################################################################

import re
#from urllib.request import urlopen
import urllib2
from bs4 import BeautifulSoup

#as of 4/7 there are only three pages of exchanges
#this has been updated to reflect the four pages

soup1 = BeautifulSoup(urllib2.urlopen('http://redditgifts.com/exchanges').read())

soup2 = BeautifulSoup(urllib2.urlopen('http://redditgifts.com/exchanges/?page=2').read())

soup3 = BeautifulSoup(urllib2.urlopen('http://redditgifts.com/exchanges/?page=3').read())

soup4 = BeautifulSoup(urllib2.urlopen('http://redditgifts.com/exchanges/?page=4').read())

##############################################################################
##############################################################################
#####the below is needed for PART ONE and PART TWO
##############################################################################
##############################################################################

exchangeLinks1 = soup1.findAll("a", {"class": "exchangelink"})
exchangeLinks1 = exchangeLinks1[::-1] #reverses the list so most recent is last

exchangeLinks2 = soup2.findAll("a", {"class": "exchangelink"})
exchangeLinks2 = exchangeLinks2[::-1]

exchangeLinks3 = soup3.findAll("a", {"class": "exchangelink"})
exchangeLinks3 = exchangeLinks3[::-1]

exchangeLinks4 = soup4.findAll("a", {"class": "exchangelink"})
exchangeLinks4 = exchangeLinks4[::-1]

allExchangeLinks = exchangeLinks4 + exchangeLinks3 + exchangeLinks2 + exchangeLinks1

exchangeNames = [] #this will store the name of all exchanges

for linkElement in allExchangeLinks:
	# elementExchangeName = str(linkElement).replace("</a>", "")
	# for 
	elementExchangeName = str(linkElement.getText())
	exchangeNames.append(elementExchangeName)


##############################################################################
###############################PART ONE#############################################
#####this will print the code needed to make the drop-down exchanges box in js

# #for the dropbox, we'll display the most recent first, so we reverse the list again
# exchangeNamesByRecent = exchangeNames[::-1]
#  
# for name in exchangeNamesByRecent:
#     print "<option>" + name + "</option>"
	
##############################################################################
################################PART TWO#######################################
#####this will print the code needed to numerical exchange lookup table in js

###for share link table, add lowercase condition

  #   index = 0
  #   name = ""
  # # print exchangeNames 
  #   for index, name in enumerate(exchangeNames[:-1]): #loops through all but last element in list
  #       print '"' + name.lower()+ '": ' + str(index) + ','
  #   print '"' + exchangeNames[-1].lower() + '": ' + str(index+1)

# #same but not lowercase:
#     name = ""
#   # print exchangeNames 
#     for index, name in enumerate(exchangeNames[:-1]): #loops through all but last element in list
#             print '"' + name + '": ' + str(index) + ','
#         print '"' + exchangeNames[-1] + '": ' + str(index+1)



### this prints the numbers to exchange lookup table:
# name = ""
# # print exchangeNames 
# for index, name in enumerate(exchangeNames[:-1]): #loops through all but last element in list
#     print '"' + str(index)+ '": "' + name.lower() + '",'
# print '"' + str(index+1) + '": "' + exchangeNames[-1].lower() +'"'


##############################################################################
###############################PART THREE#####################################

exchangeImages1 = soup1.find_all(src=re.compile("exchange-logo"))
exchangeImages1 = exchangeImages1[::-1] #reverses the list so most recent is last

exchangeImages2 = soup2.find_all(src=re.compile("exchange-logo"))
exchangeImages2 = exchangeImages2[::-1] #reverses the list so most recent is last

exchangeImages3 = soup3.find_all(src=re.compile("exchange-logo"))
exchangeImages3 = exchangeImages3[::-1] #reverses the list so most recent is last

exchangeImages4 = soup4.find_all(src=re.compile("exchange-logo"))
exchangeImages4 = exchangeImages4[::-1] #reverses the list so most recent is last

allImages = exchangeImages4 + exchangeImages3 + exchangeImages2 + exchangeImages1

allImageURLs = []

for imageURL in allImages:
    allImageURLs.append(imageURL["src"])
    # str(imageURL).replace('<img src="',"")
    # str(imageURL).replace('" width="100"/>',"")

#####this will print the code needed lookup the image url by exchange number
index = 0
for index, imageURL in enumerate(allImageURLs[:-1]): #loops through all but last element in list
    print '"' + str(index) + '": "' + imageURL + '",'
print '"' + str(index+1) + '": "' + allImageURLs[-1] +'"'