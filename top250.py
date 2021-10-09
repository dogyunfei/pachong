import requests
import re
url='https://movie.douban.com/top250'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'}
response=requests.get(url=url,headers=headers)
# print(response.text)
pageContent=response.text
#解析数据
obj=re.compile(r'<li>.*?<span class="title">(?P<name>.*?)'
               r'</span>.*? <p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
               r'property="v:average">(?P<score>.*?)</span>.*?'
               r'</span><span>(?P<comment>)</span>'
               ,re.S)
result=obj.finditer(pageContent)
for i in result:
    print(i.group('name'))
    # print(i.group('year'))
    # print(i.group('score'))
    # print(i.group('comment'))
print('over')
response.close()
