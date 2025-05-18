from selenium import webdriver

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