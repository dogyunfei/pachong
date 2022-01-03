import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

web = Chrome()

url = 'http://10.160.63.9/'
web.get(url)
# time.sleep(1)
web.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[2]/select/option[4]').click()

# time.sleep(1)
web.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[2]/form/input[2]').send_keys('21200107230')

# time.sleep(1)
web.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[2]/form/input[3]').send_keys('316417', Keys.ENTER)
# time.sleep(3)
# web.find_element(By.XPATH,'//*[@id="edit_body"]/div[1]/div[1]/form/input').click()

