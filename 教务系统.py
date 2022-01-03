from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from chaojiying import Chaojiying_Client

web=Chrome()

url='http://jw.usts.edu.cn/default2.aspx'
web.get(url=url)
zhang_hao='21200107230'
mi_ma='hyf242526.'

#处理验证码
img=web.find_element(By.XPATH,'//*[@id="txtUserName"]').screenshot_as_png
chaojiying = Chaojiying_Client('1844025705', '123456', '927188')
dic=chaojiying.PostPic(img, 1902)
verify_code=dic['pic_str']

#向页面中填入用户名和密码
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="txtUserName"]').send_keys(f'{zhang_hao}')
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="TextBox2"]').send_keys(f'{mi_ma}')
#输入验证码
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="txtSecretCode"]').send_keys(f'{verify_code}')

# #点击登录
web.find_element(By.XPATH,'//*[@id="Button1"]').send_keys(Keys.ENTER)
time.sleep(1000)


