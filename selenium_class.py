from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

class SeleniumCommon:
    
    
    def __init__(self):
        self.url = ""

        
    def access(self, url):
        driver.get(url)
        
    def find(self, element, factor):
        match element:
            case "XPATH":
                driver.find_element(By.XPATH, factor)
            case "ID":
                driver.find_element(By.ID, factor)
            case "CLASS_NAME":
                driver.find_element(By.CLASS_NAME, factor)
            case "LINK_TEXT":
                driver.find_element(By.LINK_TEXT, factor)
            case "TAG_NAME":
                driver.find_element(By.TAG_NAME, factor)
            case "CSS_SELECTOR":
                driver.find_element(By.CSS_SELECTOR, factor)
            case "PARTIAL_LINK_TEXT":
                driver.find_element(By.PARTIAL_LINK_TEXT, factor)
            