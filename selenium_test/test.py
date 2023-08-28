from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# # 指定驱动程序所在路径
driver_path = '/home/lixiang/notes/test/selenium_test/chromedriver_linux64/chromedriver'
service = Service(executable_path=driver_path)
# # 创建Chrome浏览器实例
# browser = webdriver.Chrome(service=service)

# # 打开网页
# browser.get("https://www.baidu.com")
# time.sleep(3)
# news_link = browser.find_element("link text", "图片")
# news_link.click()
# time.sleep(3)
# search_box = browser.find_element(By.ID, "kw")
# search_box.send_keys("理想汽车")
# time.sleep(3)
# button = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div/div/div/div/div/div[2]/form/span[2]/input")
# button.click()
# time.sleep(3)
# browser.quit()

# browser.get("https://image.baidu.com/")
# search_box = browser.find_element(By.ID, "kw")
# search_box.send_keys("理想汽车")
# time.sleep(3)
# button = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div/div/div/div/div/div[2]/form/span[2]/input")
# button.click()
# time.sleep(3)


import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys   # 模拟键盘输入

# # # 创建Chrome浏览器实例
# web = Chrome(service=service)

# # # 打开网页
# web.get("https://www.baidu.com")
# news_link = web.find_element("link text", "图片")
# news_link.click()
# time.sleep(1)
# web.find_element('xpath', '//*[@id="kw"]').send_keys("理想汽车")
# time.sleep(1)
# web.find_element('xpath', '/html/body/div[1]/div[1]/div[3]/div/div/div/div/div/div[2]/form/span[2]/input').click()
# time.sleep(3)
# web.quit()

# 1.创建浏览器对象
web = Chrome(service=service)

# 2.打开一个网址
web.get('http://lagou.com')

# 定位到地址：北京，然后点击他
el = web.find_element('xpath','//*[@id="changeCityBox"]/ul/li[1]/a') #这是新版的，旧版是：find_element_by_xpath
el.click() # 点击事件
time.sleep(3)

# # 搜索框输入：python ,输入回车/点击搜索按钮
# web.find_element('xpath','//*[@id="search_input"]').send_keys('python',Keys.ENTER) # Keys.ENTER是回车
# time.sleep(3)
web.find_element('xpath', '//*[@id="search_input"]').send_keys('python')
web.find_element('xpath', '//*[@id="search_button"]').click()

# # 点击第一个岗位跳转一个新页面
web.find_element('xpath','//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
time.sleep(3)


# # 切换到新窗口，在selenium中，默认不切换到新的窗口的
web.switch_to.window(web.window_handles[-1]) # 切换到最后一个窗口

# # 切换窗口后，输出该页面的岗位职责
job_detail = web.find_element('xpath','//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)

web.close()  # 关闭当前浏览器页面

web.switch_to.window(web.window_handles[0])  # 重新定位到第一个页面

# # 验证是否切换到第一个窗口
job_name = web.find_element('xpath','//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text
print(job_name)


