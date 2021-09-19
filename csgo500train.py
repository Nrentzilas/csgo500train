from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time



chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)


driver.get("https://csgo500.com/wheel")
time.sleep(2)

trainicon = driver.find_element_by_class_name("hypetrain-icon")
bux_count = driver.find_element_by_id("balance")


actions = ActionChains(driver)
actions.click(trainicon)



for i in range(500000):
      actions.perform()
      print("Successfully joined the train!")
      count = (bux_count.text)
      print('Current Balance: ' + count +' Bux')
      time.sleep(120)
