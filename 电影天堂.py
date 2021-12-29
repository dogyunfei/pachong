import requests
import re
url='https://dy.dytt8.net/index.htm'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'}
requests.packages.urllib3.disable_warnings()
response=requests.get(url=url,verify=False,headers=headers)
response.encoding='gb2312'
obj1=re.compile(r'>最新电影更新.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2=re.compile(r"<a href='(?P<href>.*?)'",re.S)
result1=obj1.finditer(response.text)
list=[]
for i in result1:
    ul=i.group('ul')

result2=obj2.finditer(ul)
for j in result2:
    chhildHref=url.replace('/index.htm','')+j.group('href')
    # print(chhildHref)
    list.append(chhildHref)
print(list)

# for href in list:
#     childResponse=requests.get(url=href,verify=False,headers=headers)
#     childResponse.encoding='gb2312'
#     print(childResponse.text)
#     break



response.close()