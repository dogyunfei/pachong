#1.拿到主页面的源代码，然后提取到子页面的链接地址，href
#2.通过href拿到子页面的内容，从子页面中找到图片的下载地址 img->src
#3.下载图片
import requests
from bs4 import BeautifulSoup
url="https://www.umei.cc/bizhitupian/weimeibizhi/"
response=requests.get(url)
# print(response.text,)会产生乱码 下面解决
response.encoding="utf-8"
# print(response.text)解决完成
#把源代码交给bs4
main_page=BeautifulSoup(response.text,"html.parser")
alist=main_page.find("div",class_="TypeList").find_all("a")

print(alist)

response.close()