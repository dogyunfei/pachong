import requests
url='https://fanyi.baidu.com/sug'
s=input('请输入')
dic={'kw':s}
response=requests.post(url,data=dic)
print(response.json())      #==>dict