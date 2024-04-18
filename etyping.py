from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui


url = "https://www.e-typing.ne.jp/roma/check/"

webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

wait = WebDriverWait(driver=driver, timeout=30)
locator = (By.XPATH,'//*[@id="start_btn"]')
driver.get(url)
#wait.until(EC.presence_of_all_elements_located)
time.sleep(3)
driver.find_element(By.ID,"level_check_btn").click()
print("今すぐチェックを押したよ")
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
#wait.until(EC.presence_of_all_elements_located)
time.sleep(5)

iframe = driver.find_element(By.XPATH,'//*[@id="typing_content"]')
driver.switch_to.frame(iframe)

start = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "start_btn")))
start.click()
print("スタートを押したよ")
time.sleep(3)
pyautogui.press('space')
time.sleep(4)

while True:
    try:
        type_text_element = driver.find_element(By.XPATH, '//*[@id="sentenceText"]/div/span[2]')
        type_text = type_text_element.text
        pyautogui.typewrite(type_text, interval=0.05)
        time.sleep(0.5)
    except NoSuchElementException:
        print("Element not found. Finishing...")
        break

    
input("Press Enter to quit...")

driver.quit()