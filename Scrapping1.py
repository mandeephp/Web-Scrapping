# fetch links from any website

from bs4 import BeautifulSoup
import urllib
handle=urllib.urlopen("")
web_data=handle.read()
soup=BeautifulSoup(web_data)
links=soup("a")
for link in links:
    if len(link.contents)>=1:
        print link.contents[0]
