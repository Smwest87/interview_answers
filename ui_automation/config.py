from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpaths import paths
import time
from credentials import creds

class Driver():
    
    def __init__(self):
        
        #url that we wish to navigate to
        self.url = 'https://shop.shipt.com/login'

        #test address
        self.address ="4832 Keith Dr Brimingham AL 35242"
        self.street ="4832 Keith Dr" 
        self.city ="Birmingham"
        self.state ="AL"
        self.zip ="35242"
        
        #browser we want to use
        self.wd = webdriver.Chrome()
        
    def open_url(self):
        self.wd.get(self.url)

    def get_address(self):
        return self.address

    def get_street(self):
        return self.street

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip

    def wait_until(self, xpath):
        try:
            element = WebDriverWait(self.wd, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except:
            print("Element did not display!")

    def find_element(self,xpath):
        return self.wd.find_element_by_xpath(xpath)        

    def login(self):
        self.wait_until(paths['login_paths']['username'])
        user = self.wd.find_element_by_xpath(paths['login_paths']['username'])
        user.send_keys(creds['username'])
        password = self.wd.find_element_by_xpath(paths['login_paths']['password'])
        password.send_keys(creds['password'])
        button = self.wd.find_element_by_xpath(paths['login_paths']['button'])
        button.click()
        self.wait_until(paths['navigation_paths']['product_cards'])