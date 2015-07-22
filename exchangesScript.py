### exchange output text for redditgiftsmap
##from bs4 import BeautifulSoup
##import urllib.request
##
##### might need more pages depending on update time
##link1 = "https://www.redditgifts.com/exchanges/?page=1"
##page1 = urllib.request.urlopen(link1)
##link2 = "https://www.redditgifts.com/exchanges/?page=2"
##page2 = urllib.request.urlopen(link2)
##link3 = "https://www.redditgifts.com/exchanges/?page=3"
##page3 = urllib.request.urlopen(link3)
##link4 = "https://www.redditgifts.com/exchanges/?page=4"
##page4 = urllib.request.urlopen(link4)
##link5 = "https://www.redditgifts.com/exchanges/?page=5"
##page5 = urllib.request.urlopen(link5)
##
##redditInfo = BeautifulSoup(page1.read() + page2.read() + page3.read() + page4.read() + page5.read(), "html.parser")
##exchanges = redditInfo.find_all('span')
##
##print(exchanges)
##
##for exchange in exchanges:
##    print(exchange.string)
##
##exchangesTxt = open('newExchanges.txt','w')
##
##exchangesTxt.close()

#assumes newExchanges.txt is file with a list of exchanges in this example format:
#"162": "magnets 2015",
#"163": "yarn 2015",

exchangesTxt = open('newExchanges.txt','r')
exchangesTxt2 = open('exchanges2.txt', 'w')
exchangesTxt3 = open('exchanges3.txt', 'w')
exchangesTxt4 = open('exchanges4.txt', 'w')
exchangesTxt5 = open('exchanges5.txt', 'w')

string5 = ""

for exchange in exchangesTxt:
    if exchange != "": #check for empty lines
        exchange = exchange.split(":")
        num = exchange[0][1:]
        num = num[:-1]
        name = exchange[1][2:]
        name = name[:-3]
        ###building file for part 2:
        exchangesTxt2.write('"' + name.title() + '": ' + num + ',\n')
        ###building file for part 3:
        exchangesTxt3.write('"' + num + '": "url here",\n' )
        ####building file for part 4:
        exchangesTxt4.write('"' + name + '": ' + num + ',\n')
        ###building string for file for part 5:
        string5 = '<option>' + name.title() + '</option>\n' + string5

        
        

exchangesTxt.close()
exchangesTxt2.close()
exchangesTxt3.close()
print("don't forget to add in the actual image urls!")
exchangesTxt4.close()
exchangesTxt5.write(string5)
exchangesTxt5.close()
        
