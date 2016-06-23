# fetch headline from any website

from bs4 import BeautifulSoup
import urllib
handle=urllib.urlopen("")
headlines=handle.read()
soup=BeautifulSoup(headlines)
headlines=soup("h3")
for head in headlines:
    if len(head.contents)>=1:
        print head.contents[0]
