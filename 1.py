import requests
import re
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400',
}
l = []
l1=[]
fid='1613906145310'
lid='0'
for i in range(0,150):
    url = 'https://coral.qq.com/article/5963339045/comment/v2?callback=_article5963339045commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+lid+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+fid
    data = requests.get(url, headers=headers).content.decode()
    con='content":"(.*?),"'
    l= re.findall(con,data,re.S)
    l1.append(l)
    pat='"last":"(.*?)"'
    lid=re.findall(pat,data,re.S)[0].replace("\n","").replace(" ","")
    fid=str(int(fid)+1)
with open('t.txt', 'a' ,encoding='utf-8') as file:
    file.write(str(l1))
import io
import jieba
import json
txt = io.open("t.txt", "r", encoding='utf-8').read()
W  = jieba.lcut(txt)
counts = {}
for w in W:
     if len(w) == 1:
         continue
     else:
        counts[w] = counts.get(w,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
List = []
for i in range(len(items)):
    Dict = {}
    w, count = items[i]
    if count >= 10:
        Dict['name'] = w
        Dict['value'] = count
        List.append(Dict)
d = {}
d['d'] = List
print(d)
with open('zyq.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)

