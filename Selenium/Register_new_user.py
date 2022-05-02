import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path=r"D:/Software development/Backend-python/Selenium/chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://demo-store.seleniumacademy.com/")
        
    def test_new_useer(self):
        driver = self.driver
        driver.find_element(by=By.XPATH, value='//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element(by=By.LINK_TEXT, value='Log In').click()
        create_account_button = driver.find_element(by=By.XPATH, value='//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        print(create_account_button)
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        self.assertEqual('Create New Customer Account', driver.title)
        first_name = driver.find_element_by_id('firstname')
        middle_name= driver.find_element_by_id('middlename')
        last_name=driver.find_element_by_id('lastname')
        email_adress=driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password=driver.find_element_by_id('confirmation')
        news_letter_subscription= driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="form-validate"]/div[2]/button')
        print(submit_button)
        self.assertTrue(first_name.is_enabled() 
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_adress.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())
        
        first_name.send_keys('Test')
        driver.implicitly_wait(3)
        middle_name.send_keys('Test')
        driver.implicitly_wait(3)
        last_name.send_keys('Test')
        driver.implicitly_wait(3)
        email_adress.send_keys('Test@gmail.com')
        driver.implicitly_wait(3)
        news_letter_subscription.send_keys('Test')
        driver.implicitly_wait(3)
        password.send_keys('Test')
        driver.implicitly_wait(3)
        confirm_password.send_keys('Test')
        driver.implicitly_wait(3)
        submit_button.click()
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()    
        
if __name__ == "__main__":
	unittest.main(verbosity = 2)