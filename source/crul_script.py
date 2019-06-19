import requests
from bs4 import BeautifulSoup
import nltk
import operator
from nltk.stem import WordNetLemmatizer
import sys
lemmatizer = WordNetLemmatizer()

def RemoveContent(source, tag):
    token = source.split("<%s>"%tag)
    result = token[0]
    for x in token[1:]:
        result = result + x.split("</%s>"%tag)[1]
    return result
def Multi2One(source, target, replacement=None):
    if not(replacement):
        replacement = target
    return replacement.join([x for x in source.split(target) if x!=''])

def MakeClean(source, delimiter):
    return delimiter.join([s.strip() for s in source.split(delimiter)])

def Symbol2NewOne(source, way):
    for symbol in way:
        source = source.replace(symbol,way[symbol])
    return source
def return_title(title):
    return title[30:-5]



    
input_url = sys.argv[0]
genre_page = 'https://www.imsdb.com/Movie Scripts' + input_url[29:-5].replace('-',' ')+' Script.html'
#input_url = 'https://www.imsdb.com/scripts/A-Few-Good-Men.html'
movie_title = "/Dockershare/movie/"+return_title(input_url)+".txt"
f2= open(movie_title,'a')


# 找genre and writer
req = requests.get(genre_page)
soup = BeautifulSoup(RemoveContent(str(req.content), 'b'), 'lxml')
text = soup.find('table',{'class':'script-details'})
imfor = text.find_all('a')
total = len(imfor)
writer = imfor[0]
writer = writer.text
f2.write(input_url[29:-5].replace('-',' '))
f2.write('\n')
f2.write(writer)
f2.write('\n')

for i in range(1,total-1):
    genre = imfor[i].text
    f2.write(genre)
    f2.write('/n')
    

# 找words 
req = requests.get(input_url)
soup = BeautifulSoup(RemoveContent(str(req.content), 'b'), 'lxml')

text = soup.find('td',{'class':'scrtext'}).text
text = Multi2One(text, '\\r\\n', '\\n')
text = Multi2One(text, '\\n')
text = MakeClean(text,'\\n')
text = Symbol2NewOne(text, {"\\n":"\n", "\\'":"'", "\\t":"\t"})
front = str(text)



dict_m = {'name':0 , 'for':0}


words_list = nltk.word_tokenize(front)
word_list = nltk.pos_tag(words_list,tagset='universal')
for words in word_list:


    EName = words[0]
    EDes  = words[1]
    EName = lemmatizer.lemmatize( EName ,pos = 'v')
    EName = lemmatizer.lemmatize(EName )
    EName = EName.lower()
    if EDes == '.':
        continue
    if EName in dict_m:
        value = dict_m[EName] + 1
        dict_m[EName] = value
    else:
        dict_m[EName] = 1
    
    #print(EName,EDes)
sorted_x = sorted(dict_m.items(), key=operator.itemgetter(1))
sorted_x.reverse()
for w in sorted_x:
    string = str(w)
    f2.write(string)

    f2.write("\n")

f2.close()
