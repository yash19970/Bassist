from bs4 import BeautifulSoup as bs
import urllib2
string ="dog" 
side_addr = 'https://en.wikipedia.org/wiki/'+string
response = urllib2.urlopen(side_addr)
html = response.read()
soup = bs(html,'lxml')
for div in soup.findAll('div', attrs={'id':'mw-content-text','class':'mw-content-ltr'}):
    k= div.p.text[0:250] #wikipedia data.

flag=0
k2 = "" 
for i in k:
	if i =='(' or i =='[' :
		flag =1
	elif i == ')' or i ==']':
		flag =0
	elif i == '.':
		k2= k2+i
		break
	elif i !='(' and i!=')' and flag==0:
		k2= k2+i
print k2 #sentance. 
