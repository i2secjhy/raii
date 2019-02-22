# -*- coding: cp949 -*-
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

def get_first_element(x):
    return x[1]

class Crawl :
    def __init__(self,url):
        self.url= url

    def rq(self):
        r=requests.get(self.url)
        return r.content
    
    def bs(self, content):
        r=BeautifulSoup(content,"html.parser")
        return r

class Bohemian(Crawl):

    def lyrics(self,d,i,ii):
        tag=d.find(i,ii)
        return tag.get_text()

if __name__ == "__main__" :
  
    bhma = Bohemian('https://www.songtexte.com/songtext/freddie-mercury/bohemian-rhapsody-23982857.html')
    r = bhma.rq()
    s = bhma.bs(r)
    a= bhma.lyrics(s,"div",{'id':'lyrics'})
    


    with open ("attachments/sample.txt","w") as f:
     f.write(a)
    print "크롤링 파일저장!"


    res=list()
    with open ("attachments/sample.txt","r") as g:
        data=g.read()
        parse = re.sub("[()',]",'',data)
        words=parse.lower().split()
    print "특수문자제거,소문자변환,단어수 셌다"
    


    print "옵션 선택해주세요 ^^"
    r=input()




if r == '-c' :
    D={}
    for word in words:
        if word in D:
            D[word] += 1
        else:
            D[word] = 1
    for key in D:
        print key,':',D[key]
elif r == '-h':
    res={}
    for word in words:
        res[word] = words.count(word)

    tup = res.items()
    tup.sort(key=get_first_element, reverse=True)

    d = list()
    for k,v in tup:
        tmp = k+"\t:"+"*"*v
        d.append(tmp)
    print "\n".join(d)+'\n'

elif r == '-t':
    res={}
    for word in words:
        res[word] = words.count(word)

    tup = res.items()
    tup.sort(key=get_first_element, reverse=True)

    d = list()
    for k,v in tup:
        tmp = k+"\t:"+"*"*v
        d.append(tmp)

        
    print "\n".join(d[:5])+'\n'

else:
    print "unknown option"
    print " usage:python [filename] {-c | -h | -t} [target]"


