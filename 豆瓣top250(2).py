import time

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import csv

file=open('data.csv',mode='w',encoding="utf-8",newline='')
csvwriter=csv.writer(file)


def download_one_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"}
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    html = etree.HTML(response.text)

    grid_view = html.xpath("/html/body/div[3]/div[1]/div/div[1]/ol")[0]

    xu_hao=grid_view.xpath("./li/div[1]/div/em/text()")
    title=grid_view.xpath("./li/div[1]/div[2]/div[1]/a/span[1]/text()")
    # print(title)
    # print(xu_hao)
    ls=[]
    for i in range(len(title)):
        ls.append([xu_hao[i],title[i]])
    # print(ls[0])
    for i in ls:
        csvwriter.writerow(i)
    file.close()
    print(url,'提取完毕')


if __name__ == '__main__':
    for i in range(226,25):
        url = "https://movie.douban.com/top250?start={}&filter=".format(i)
        download_one_page(url=url)
    print('全部下载完成')

# #多线程
# if __name__ == '__main__':
#     with ThreadPoolExecutor(1) as t:
#         for i in range(0,226,25):
#             print(i)
#             t.submit(download_one_page,f"https://movie.douban.com/top250?start={i}&filter=")
#             time.sleep(5)
#     print('全部下载完毕')
