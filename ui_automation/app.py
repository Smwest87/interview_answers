from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from xpaths import paths
import time
from config import Driver
from credentials import creds

driver = Driver()
driver.open_url()
driver.login()

#navigate to account and attempt to add a new address
account = driver.find_element(paths['navigation_paths']['account'])
account.click()
driver.wait_until(paths['navigation_paths']['profile_name'])
address_tab = driver.find_element(paths['navigation_paths']['address_tab'])
address_tab.click()
driver.wait_until(paths['navigation_paths']['address_card'])
add_address = driver.find_element(paths['navigation_paths']['add_address'])
add_address.click()
address_autocomplete = driver.find_element(paths['navigation_paths']['address_autocomplete'])
address_autocomplete.click()
address_autocomplete.send_keys(driver.get_address())
driver.wait_until(paths['navigation_paths']["auto_complete_option"])
option = driver.find_element(paths['navigation_paths']["auto_complete_option"])
option.click()
#assert each field is populated accurately 
street1 = driver.find_element(paths['navigation_paths']['street'])
#so when I am debugging value has a a string attached to it. But when the script actually runs there is no value.Need to research further
value = street1.get_attribute('value')
street = driver.get_street()
if value == street:
    (print('All Clear'))
else: 
    print(value)
    print(street)
#save -- going too fast here , need to figure out an implicit wait
time.sleep(2)
save = driver.find_element(paths['navigation_paths']['address_save'])
save.click()
#-- going too fast here , need to figure out an implicit wait
time.sleep(5)

driver.wd.get('https://shop.shipt.com/account/addresses')
driver.wait_until(paths['navigation_paths']['address_card'])
driver.wait_until(paths['navigation_paths']['new_address_card'])

#need to delete the address afterwards -- cleanup step