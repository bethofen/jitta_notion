from selenium import webdriver
import time
import pickle
import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run headless for no GUI
    user_data_dir = r"C:\Users\beatk\AppData\Local\Google\Chrome\User Data\Profile 16"

    options.add_argument(f"user-data-dir={user_data_dir}")

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("window-size=1000,600")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-application-cache')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--mute-audio")
    options.add_argument('--disable-notifications')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    return driver



if os.path.isfile("cookies.pkl"):
    driver = get_driver()
    driver.get("https://www.jitta.com/explore?country%5B0%5D=US")
    time.sleep(1)
    
        
    # # Send PAGE DOWN using the BODY element
    # body = driver.find_element(By.TAG_NAME, 'body')

    # # Send PAGE DOWN key multiple times
    # for _ in range(30):
    #     body.send_keys(Keys.PAGE_DOWN)
    #     time.sleep(0.1)
        
    print("All data loaded.")

    # block_data = driver.find_element(By.XPATH, "//div[contains(@class, 'FilterResults__ResultsWrapper-lnmeq7-0')]")
    block_datas = driver.find_elements(By.XPATH, "//div[contains(@class, 'FadeInAnimationChild__FadeInWrapper-w3yuus-0')]")
    print(len(block_datas))
    for i in block_datas:   
        name = i.find_element(By.XPATH, ".//div[contains(@class, 'Text__TextXS-dn2wcp-3')]")
        score = i.find_element(By.XPATH, ".//h2[contains(@class, 'Heading__HeadingLG-sc-1wavirx-1')]")
        percen = i.find_element(By.XPATH, ".//div[contains(@class, 'JittaLine__JittaLineBlock-fitgha-0')]")
        # percenUpDown = i.find_element(By.XPATH, ".//div[contains(@class, 'Text__TextXS-dn2wcp-3')]")
        print(f"{name.text} {score.text}  {percen.text.split("\n")} ")



print("not found file") 


# driver = get_driver()
# driver.get("https://accounts.jitta.com/login?applicationName=jittadotcoms&redirectUrl=/home")
# time.sleep(15)
# email_input = driver.find_element("xpath", "//input[@name='email']")
# email_input.send_keys("beatkingphoto@gmail.com")
# pass_input = driver.find_element("xpath", "//input[@name='password']")
# pass_input.send_keys("#BestJitta321")
# time.sleep(1)
# login_button = driver.find_element("xpath", "//button[text()='เข้าสู่ระบบ']")
# login_button.click()
# time.sleep(2)

# session_cookies = driver.get_cookies()
# # Save the serialized cookies to a file
# with open("cookies.pkl", "wb") as f:    
#     pickle.dump(session_cookies, f)
            
            
# if not os.path.isfile("cookies.pkl"):
#     if driver.title == "SET e-Learning":
#         time.sleep(1)  
#         # cookies = driver.get_cookies()
#         session_cookies = driver.get_cookies()
#         # Save the serialized cookies to a file
#         with open("cookies.pkl", "wb") as f:    
#             pickle.dump(session_cookies, f)