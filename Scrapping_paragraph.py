# fetch paragraph from any website

from bs4 import BeautifulSoup
import urllib
handle=urllib.urlopen("")
paragraph=handle.read()
soup=BeautifulSoup(paragraph)
paragraph=soup("h3")
for para in paragraph:
    if len(para.contents)>=1:
        print para.contents[0]
