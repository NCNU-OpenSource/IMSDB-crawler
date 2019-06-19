import requests
from bs4 import BeautifulSoup


f = open('/Dockershare/list.txt', 'a')
req = requests.get("https://www.imsdb.com/alphabetical/A")
soup = BeautifulSoup(req.content,features="html.parser")
i=0
for tag in soup.findAll('p'):
    tag = tag.a['href']
    #print(tag)
    tag = tag[14:]
    tag = tag.replace(' Script','')
    tag = tag.replace(' ','-')
    #print(tag)

    href = "https://www.imsdb.com/scripts"+tag

    print(href)
    href = href + " 0\n"
    f.write(href)
