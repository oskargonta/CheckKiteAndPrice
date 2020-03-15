from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select, expected_conditions
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import time

#CREATE WEBROWSER
driver = webdriver.Chrome(r'C:\Users\gonta\PycharmProjects\Selenium\seleniumddemo\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.getakite.de')

#DETAILSUCHE
driver.find_element_by_id('show_advanced_searchform').click()

#CATEGORY
driver.find_element_by_id('id_category').click()
id_cat_select = Select(driver.find_element_by_id('id_category'))
id_cat_select.select_by_value('1')

#MODEL_KITE
driver.find_element_by_id("id_keyword").click()
driver.find_element_by_id("id_keyword").clear()
driver.find_element_by_id("id_keyword").send_keys ('Soul')

#COMPANY_SELECT
driver.find_element_by_id('id_factory').click()
company_select = Select(driver.find_element_by_id('id_factory'))
company_select.select_by_visible_text('Flysurfer')

#PRICE_RANGE
driver.find_element_by_id('id_price_0').send_keys('1000')
driver.find_element_by_id('id_price_1').send_keys('1800')

#YEAR_RANGE
year_from_prod_select = Select(driver.find_element_by_id('id_year_0'))
year_from_prod_select.select_by_value('18')
year_to_prod_select = Select(driver.find_element_by_id('id_year_1'))
year_to_prod_select.select_by_value('21')

#SIZE_RANGE
from_size_select = Select(driver.find_element_by_id('id_kitesize_0'))
from_size_select.select_by_value('34')
to_size_select = Select(driver.find_element_by_id('id_kitesize_1'))
to_size_select.select_by_value('37')

#CLICK_SUBMIT
submit_button = driver.find_element_by_xpath("//button[@type='submit']").click()
driver.implicitly_wait(10)

#PRINT OFERTS_NAMES
oferts = driver.find_elements_by_xpath(".//h3[contains(@class,'margin-clear bold')]//a")
ofert_names = [ofert.get_attribute("text") for ofert in oferts]
for name in ofert_names:
    print("Ofert name: " + name)

print("pierwszy element", ofert_names[0])

#PRINT PRICES
prices = driver.find_elements_by_xpath("//div[contains(@class,'mt-20')]//span")
price_values = [price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("Cena to: " + price)

#ASERCJA NAZW
# assert ofert_names[0] == 'Flysurfer Soul 15 qm Neuwertig'
# assert ofert_names[1] == 'Flysurfer Soul 12m 2019'
# assert ofert_names[2] == 'Kite Flysurfer Soul 12m2'
# assert ofert_names[3] == 'Flysurfer Kite Ausrüstung'

driver.quit()
