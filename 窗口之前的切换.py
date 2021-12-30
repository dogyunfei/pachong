from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web = Chrome()
url = 'http://lagou.com'
web.get(url=url)
web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a').click()
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys('python', Keys.ENTER)

# 新窗口
web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()

#切换窗口

web.switch_to.window(web.window_handles[-1])
job_details=web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div').text
print(job_details)

#关掉子窗口
web.close()
web.switch_to.window(web.window_handles[0])
text=web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text()
print(text)
web.close()