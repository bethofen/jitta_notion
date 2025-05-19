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

class basic_back_test:
    def __init__(self):
        self.reset()
    def run_backtest(self):
       pass    
    def close_order(self,close_price):
        if self.current_position == "BUY":
            pre_profit = close_price - self.open_position_price
            self.list_trade.append(pre_profit)                                                                                                                                                                         
            self.percen_trade.append(pre_profit / self.open_position_price * 100)
        elif self.current_position == "SELL":
            pre_profit = self.open_position_price - close_price
            self.list_trade.append(pre_profit)  
            self.percen_trade.append(pre_profit / self.open_position_price * 100)
        else:
            raise ValueError("nope")
        
        self.open_position_price = None
        self.switch_free +=1  
        self.current_position = None
        data = self.data.iloc[self.i]
        self.detail_trade["close_date"] = data["datetime"]
        self.detail_trade["close_price"] = close_price
        self.detail_all_trade.append(self.detail_trade)
        self.detail_trade = {}
    def get_order(self,position,open_price):
        self.current_position = position
        self.open_position_price = open_price
        data = self.data.iloc[self.i]
        self.detail_trade["position"] = position
        self.detail_trade["open_date"] = data["datetime"]
        self.detail_trade["open_price"] = open_price
  
    def reset(self):
        self.current_position = None
        self.open_position_price = None
        self.trailing_stop = None
        self.list_trade = []
        self.switch_free = 0
        self.multiply_stop = 2
        self.percen_trade = []
        self.detail_trade = {}
        self.detail_all_trade = []
    def load_data(self,data):
        self.data = data
    def find_avg_order(self):
        all_position = ['high','low','close','open']
        all_position = [self.data.iloc[self.i][po] for po in all_position]
        return sum(all_position) / len(all_position)    
    def get_history(self):
        return self.list_trade
    def get_percen(self):
        return self.percen_trade
    def get_detailAllTrade(self):
        return self.detail_all_trade