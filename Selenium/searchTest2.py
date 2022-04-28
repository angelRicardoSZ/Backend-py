import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class SearchTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:/Software development/Backend-python/Selenium/chromedriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)
        
    def test_search_tee(self):
        driver  = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        
        search_field.send_keys("tee")
        search_field.submit()
        
    def test_search_salt_shaker(self):
        driver  = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.send_keys("salt shaker")
        search_field.submit()
        
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li/div')
        self.assertEqual(1,len(products))
    
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output="reportes",report_name="search2_test_report"))
    