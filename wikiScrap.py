from bs4 import BeautifulSoup as bs
import urllib2
string ="dog" 
side_addr = 'https://en.wikipedia.org/wiki/'+string
response = urllib2.urlopen(side_addr)
html = response.read()
soup = bs(html,'lxml')
for div in soup.findAll('div', attrs={'id':'mw-content-text','class':'mw-content-ltr'}):
    print div.p.text[0:150] #wikipedia data.
