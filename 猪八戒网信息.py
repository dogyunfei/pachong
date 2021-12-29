#导入模块
import requests
from lxml import etree

#拿到网页源代码
url="https://suzhou.zbj.com/search/f/?kw=saas"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"}
response=requests.get(url=url,headers=headers)
# print(response.text)
#解析
html=etree.HTML(response.text)

#拿到每一个服务商
divs=html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")

for div in divs:    #每一个服务商信息
    price=div.xpath("./div/div/a/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title=div.xpath("./div/div/a/div[2]/div[2]/p/text()")
    companyName=div.xpath("./div/div/div[1]/div[1]/@data-shopname")
    space=div.xpath("./div/div/a[1]/div/div/span/text()")
    print(price,end=' ')
    print(title,end=' ')
    print(companyName,end=' ')
    print(space)


