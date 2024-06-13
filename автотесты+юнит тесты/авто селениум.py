from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get('https://www.qa-practice.com/elements/button/simple')
# click_button = browser.find_element(By.CLASS_NAME,'btn-primary')
# click_button.click()
# link = browser.find_element(By.LINK_TEXT,'Contact')
# browser.execute_script('arguments[0].click();',link)
# click_button2 = browser.find_element(By.CSS_SELECTOR,'input[class="btn btn-primary"]').click()
click_button4 = browser.find_element(By.XPATH,'//input[@class="btn btn-primary"]').click()
sleep(5)
