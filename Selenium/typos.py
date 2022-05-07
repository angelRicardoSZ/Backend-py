import unittest
from selenium import webdriver

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text("Typos").click()
        
    def test_name_elements(self):
        driver = self.driver
        
        paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        text_to_check = paragraph_to_check.text
        
        tries = 1
        found = False
        correct_text ="Sometimes you'll see a typo, other times you won't."
        
        while text_to_check != correct_text:
            print("text to check")
            print(text_to_check)
            print("text correct")
            print(correct_text)
        
            paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            print("text to check update")
            print(text_to_check)
            driver.refresh()
        while not found:
            if text_to_check == correct_text:
                tries += 1
                print(tries)
                driver.refresh()
                found = True
        self.assertEqual(found,True)
        
        print(f"It took {tries} tries to find the typo")
        
            
    def tearDown(self):
        self.driver.close()
           
if __name__ == "__main__":
	unittest.main(verbosity = 2)
 
 