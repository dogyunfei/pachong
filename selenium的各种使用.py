import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

web = Chrome()

url = "https://www.lagou.com/"

web.get(url=url)

# 找到某个元素，点击它
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
# el=web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()  # 点击操作
# time.sleep(1)
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("python", Keys.ENTER)

# 查找存放数据的位置，进行数据提取
# 找到页面中存放数据的所有li

divs_list = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')
for div in divs_list:
    name = div.find_element_by_tag_name('a').text 
    print(name)
