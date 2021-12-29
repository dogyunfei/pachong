import requests
import re
import csv

url='https://movie.douban.com/top250'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'}
response=requests.get(url=url,headers=headers)
pageContent=response.text
#解析数据
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
               r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
               r'.*?property="v:average">(?P<average>.*?)</span>'
               r'.*?</span>.*?<span>(?P<comment>.*?)</span>'
               ,re.S)
result=obj.finditer(pageContent)
file=open('top250.csv',mode='w',newline='')
csvwriter=csv.writer(file)
for i in result:
    # print(i.group('name'))
    # print(i.group('year').strip())
    # print(i.group('average'))
    # print(i.group('comment'))
    dic=i.groupdict()
    dic['year']=dic['year'].strip()
    csvwriter.writerow(dic.values())
file.close()
response.close()
print('over')
