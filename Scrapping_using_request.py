# To get content from a website

import requests
from bs4 import BeautifulSoup
r=requests.get("www.example.com")
r.content
