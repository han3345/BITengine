import sys
from bs4 import BeautifulSoup

html=open('bitren.html','r')
soup=BeautifulSoup(html,parser='lxml')

links=[node.get('href') for node in soup.find_all("a")]

with open('bitrenLinks.txt','w') as f:
    sys.stdout=f
    for link in links:
        print(link)

