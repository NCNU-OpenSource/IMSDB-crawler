import requests
from bs4 import BeautifulSoup
#import datetime
#today = datetime.date.today()
#yesterday = today - datetime.timedelta(days = 1)
#today_date = str(today)+'.txt'
#yes_date = str(yesterday)+'.txt'

list_check = []
f = open('/Dockershare/list.txt', 'a+')
#f = open(date, 'r+')
for row in f:
    row = row.split(' ')[0]
    list_check.append(row)
req = requests.get('https://www.imsdb.com/latest/')
soup = BeautifulSoup(req.content, 'lxml')

soup = soup.find_all('td',{'valign':'top'})
soup = soup[2]
soup = soup.find_all('td')
i = 0
is_create = 0
for title in soup :
    url = title.find('a')
    if i == 0:
        i += 1
        continue

    url = url.text.replace(' Script','').replace(' ','-')
    url = "https://www.imsdb.com/scripts/" + url + ".html"
    #f.write(url)
    #f.write('\n')
    if url not in list_check:
	url = url + " 0"
        f.write(url)
        f.write('\n')

    '''
    if is_diff == 1:
        for row in list_check: 
            if  row == str(url):
                f2 = open(today_date,'a+')
                is_diff = 0
                break
    if is_diff == 1:
        for row in list_check: 
            if  row == str(url):
                f2.write(url)
                f2.write('\n')
                break
    '''
    
#f2.close()
f.close()
#tag = tag.replace(' Script','')
#tag = tag.replace(' ','-')
#https://www.imsdb.com/scripts/Secret-Life-of-Walter-Mitty,-The.html

