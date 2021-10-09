import requests
url='https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=1'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'}
response=requests.get(url=url,headers=headers,)
# print(response.request.url)
# print(response.text)#拿到网页源码
print(response.json())
response.close()#关掉访问