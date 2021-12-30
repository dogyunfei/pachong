from selenium.webdriver import Chrome
web=Chrome()    #打开谷歌浏览器
web.get("http://www.baidu.com")     #访问网址
print(web.title)    #获取标题
web.close()     #关闭网页