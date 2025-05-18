from selenium import webdriver
import time
import pickle
import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from module import *

# stock_list = ["nyse:asr","nasdaq:amal","nasdaq:fcnca","nasdaq:amzn"]
stock_list = ["nyse:asr"]

x = "https://www.jitta.com/stock/"
stock_data = []
for i in stock_list:
    
    if os.path.isfile("cookies.pkl"):
        driver = get_driver()
        driver.get(f"https://www.jitta.com/stock/{i}")
        time.sleep(2)
        
        
        score = driver.find_element(By.XPATH, "//div[contains(@class, 'JittaScoreBlock__ScoreBlock-u8rkin-0')]")
        percen = driver.find_element(By.XPATH, "//div[contains(@class, 'JittaLine__JittaLineBlock-sc-1dmy69u-0')]")
        price_lossChange = driver.find_elements(By.XPATH, "//div[contains(@class, 'StockCard__HeadValue-sc-82hvpa-3')]")
        price_lossChange = [i.text for i in price_lossChange]
        # price = price_lossChange[0]
        # loss_change = price_lossChange[1]


        # factors_data = []
        # factors = driver.find_elements(By.XPATH, "//div[contains(@class, 'CustomizableWidget__ContentWrapper-p8w0s7-3') and contains(@class, 'fXjTaW')]")
        # for factor in factors:
        #     text_div = factor.find_element(By.XPATH, ".//div[contains(@class, 'Text-dn2wcp-1')]")
        #     factors_data.append(text_div.text)
            
        # signs_data = []
        # signs = driver.find_elements(By.XPATH, "//div[contains(@class, 'JittaSignMobile__OverFlowContainer-sc-7174ly-0')]")
        # for sign in signs:
        #     try:
        #         span = sign.find_element(By.XPATH, ".//span[contains(@class, 'JittaSignValue__SignLabel-sc-64dtld-1')]")
        #         span_type = span.get_attribute("type")
        #         signs_data.append(span_type)
        #         print("Type:", span_type)
        #     except:
        #         print("ไม่พบ span ภายใน factor นี้")
        score = score.text.split("\n")[0]
        stock_data.append([i,score,price_lossChange[0],price_lossChange[1]])         
        
        
        
        driver.quit()
        
print(stock_data)
