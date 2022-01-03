import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.keys import Keys
web = Chrome()
url = 'http://www.chaojiying.com/user/login/'
web.get(url=url)
zhang_hao = '1844025705'
mi_ma = '123456'

# 处理验证码

img = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client(f'{zhang_hao}', f'{mi_ma}', '927188')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']
#
# # 向页面中填入用户名和密码
# time.sleep(1)
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(f'{zhang_hao}')
# time.sleep(1)
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(f'{mi_ma}')
# time.sleep(1)
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(f'{verify_code}')
# #点击登录
#
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
time.sleep(1000)
