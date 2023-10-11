# seleniumの動作確認用で作成した翻訳ツール

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 日本語を入力する
japanese = input("英訳したい日本語を入力してください：")

# ウェブドライバの設定
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

# google翻訳のURLを開く
driver.get('https://translate.google.com/?sl=ja&tl=en&op=translate')

# テキストエリアに反映
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys(japanese)

# 翻訳待ちの時間を確保
time.sleep(5)

# 結果を出力
result = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span').text

print(result)

# ドライバーを閉じる
driver.quit()
