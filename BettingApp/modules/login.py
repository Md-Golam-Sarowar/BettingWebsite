from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pickle
import time


def login():
    url = "https://betbig247.com/"
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")

    browser = webdriver.Chrome(options=options)

    browser.get(url)

    search = browser.find_elements_by_class_name("gray_text")

    search[0].send_keys("bt18916")
    search[1].send_keys("blazer")

    logininfo = browser.find_element_by_class_name("login_contx")

    logininfo.click()

    time.sleep(2)

    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))


login()