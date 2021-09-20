from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys
from subprocess import call




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
      print('\n\nSuccessfully joined the train!\n')
      count = (bux_count.text)
      int_count = driver.find_element_by_id("balance")
      int_count = int(count.replace(',', ''))
      onebuxprice = int(6)
      bux_price = int()
      bux_price = (int_count*onebuxprice)/10000
      bux_price_str =str(bux_price)
      print('Current Balance: ' + count +' Bux , In Usd: '+ bux_price_str+'\n')
      call(["python", "Countdown.py"])
time.sleep(1)
