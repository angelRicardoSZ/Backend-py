import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver3.exe")
        driver = self.driver
        driver.get("https://www.mercadolibre.com/")
        driver.maximize_window()
        
    def test_search_ps4(self):
        driver = self.driver
        country = driver.find_element_by_id('MX')
        country.click()
        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        cookies_in = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/button[1]")
        cookies_in.click()
        sleep(3)
        location = driver.find_element_by_partial_link_text('Puebla')
        #location = driver.find_element(by=By.NAME, value='Puebla')
        print(location)
        location.click()
        sleep(3)
        
        condition = driver.find_element_by_partial_link_text('Nuevo')
        condition.click()
        sleep(3)
        
        order_menu = driver.find_element_by_class_name("andes-dropdown__standalone-arrow")
        order_menu.click()
        
        higher_price = driver.find_element_by_css_selector("#andes-dropdown-más-relevantes-list-option-price_desc > div > div > span")
        higher_price.click()
        sleep(3)
        
        
        articles = []
        prices = []
        
        #print(article_name.text)
        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            
            #article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            #article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            #article_name = driver.find_element_by_class_name('ui-search-item__title').text
            print(article_name)
            articles.append(article_name)
            #article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[1]').text
            #prices.append(article_price)
            
        #print(articles,prices)
            
        
        
        
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
	unittest.main(verbosity = 2)  