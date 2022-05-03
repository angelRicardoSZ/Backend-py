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
        
    def test_select_language(self):
        exposed_options = ['English', 'French', 'German'] # Opciones
        active_options = [] # Opciones mostradas en la página
        
        select_language = Select(self.driver.find_element_by_id('select-language')) #seleccionamos el dropdwon 
        self.assertEqual(3,len(select_language.options)) # validamos que el dropdwon tenga tres opciones
        for option in select_language.options: # estaremos agregando el texto
            active_options.append(option.text)
        self.assertEqual(exposed_options,active_options) # validamos que las opciones activas y las definidas sean las mismas       
        self.assertEqual('English',select_language.first_selected_option.text) # validamos que el idioma inglés sea el que esta por defecto
        
        select_language.select_by_visible_text('German') # seleccionamos otro idioma
        self.assertTrue('store=german' in self.driver.current_url) # validamos que se haya seleccionado
        select_language = Select(self.driver.find_element_by_id('select-language')) # nos posicionamos en el dropdown
        select_language.select_by_index(0) #seleccionamos el primer elemento

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()    
        
if __name__ == "__main__":
	unittest.main(verbosity = 2)
    
    