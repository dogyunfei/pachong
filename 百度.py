from urllib.request import urlopen
url='http://www.baidu.com'
response=urlopen(url)

file=open('百度.html','w',encoding='utf-8')
file.write(response.read().decode('utf-8'))
file.close()
print('over')

