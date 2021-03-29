import re
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExpectedConditions
import time
import pickle
import math


def leagueInformation(weburl):

    url = "https://"+weburl
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")

    browser = webdriver.Chrome('C:/Users/USER/chromedriver.exe', options=options)

    browser.get(url)

    try:
        WebDriverWait(browser, 10).until(
            ExpectedConditions.presence_of_element_located(
                (By.ID, "main-sportsbook-container")
            )
        )
    except Exception as inst:
        print("Leagues not found")

    leagueDiv = BeautifulSoup(browser.page_source, "html.parser").find(
        "div", {"id": "main-sportsbook-container"}
    )
    browser.close()
    return leagueDiv