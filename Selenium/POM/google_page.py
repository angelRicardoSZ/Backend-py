import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class GooglePage(unittest.TestCase):
    def __init__(self,driver):
        self._driver = driver
        self._url = 'https://google.com'
        self.search_locator = 'q'
        
    @property    
    def is_loaded(self):
        WebDriverWait(self._driver,10).until(EC.presence_of_element_located((By.NAME,'q')))
        return True
    
    @property
    def keyword(self):
        input_file = self._driver.find_element_by_name('q')
        return input_file.get_attribute('value')
    def open(self):
        self._driver.get(self._url)
        
    def type_search(self,keyword):
        input_field = self._driver.find_element_by_name('q')
        input_field.send_keys(keyword)
        
    def click_submit(self):
        input_field = self._driver.find_element_by_name('q')
        input_field.submit()
        
    def search(self,kewyword):
        self.type_search(kewyword)
        self.click_submit

        
        
           
if __name__ == "__main__":
	unittest.main(verbosity = 2)
 