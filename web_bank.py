import mechanize
import requests
import pandas as pd
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

url = "http://example.webscraping.com/places/default/user/login"
br = mechanize.Browser()
cj = CookieJar()
br.set_cookiejar(cj)
br.set_handle_robots(False) # ignore robots
br.open(url)
br.form = br.forms()[0]

br['email'] = ""
br['password'] = ""
br.method = "POST"
res = br.submit()
content = res.read()
print(cj)
s = requests.Session()
s.cookies = cj
r = s.get('http://example.webscraping.com/places/default/view/Afghanistan-1')
r.content

r2 = s.get('http://example.webscraping.com/places/default/user/logout?_next=/places/default/index')
print(r2.content.decode('utf-8'))


