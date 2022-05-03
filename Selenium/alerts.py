import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path=r"D:/Software development/Backend-python/Selenium/chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://demo-store.seleniumacademy.com/")
        
    def test_compare_products_remove_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()
        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()
        alert = driver.switch_to.alert
        alert_text = alert.text
        self.assertAlmostEqual('Are you sure you would like to remove all products from your comparison?',alert_text)
        alert.accept()        

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()    
        
if __name__ == "__main__":
	unittest.main(verbosity = 2)