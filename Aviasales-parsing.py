from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://www.aviasales.ru')
time.sleep(1)
out_airport = browser.find_element_by_xpath("//input[@id='origin']")
in_airport = browser.find_element_by_xpath("//input[@id='destination']")
out_airport.send_keys('Санкт-Петербург')
time.sleep(1)
in_airport.send_keys('Москва')
time.sleep(1)
data_out = browser.find_element_by_xpath("//div[@class='trip-duration__input-wrapper --departure']")
data_out.click()
time.sleep(1)
browser.find_element_by_xpath("//select[@class='calendar-caption__select']").click()
browser.find_element_by_xpath("//option[@value='2020-05']").click()
browser.find_element_by_xpath("//div[@aria-label='Fri May 01 2020']").click()
time.sleep(1)
browser.find_element_by_xpath("//button[. = 'Обратный билет не нужен']").click()
time.sleep(1)
browser.find_element_by_xpath("//button[@class='trip-duration__field-clear']").click()
time.sleep(2)
Serch = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[3]/div/div/form/div[3]/button")
Serch.click()
