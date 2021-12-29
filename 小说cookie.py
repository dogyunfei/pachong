import requests


#1.登录得到cookie
#2.带着cookie去请求到书架url
session = requests.session()
data={"loginName": "17851302691",
      "password": "hyf242526."}
url="https://passport.17k.com/ck/user/login"
response=session.post(url=url,data=data)
print(response.text)
print(response.cookies)