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
from selenium.webdriver.support.ui import Select


def dropdowninfo():
    url = "https://plive.dgs.phnserv.eu/live/?#!/home"
    title = "BASKETBALL"
    dropdown1 = "Total"
    dropdown2 = "Point spread"
    dropdown3 = "Total"
    points = []

    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")

    browser = webdriver.Chrome(options=options)

    browser.get(url)

    try:
        WebDriverWait(browser, 5).until(
            ExpectedConditions.presence_of_element_located(
                (
                    By.CLASS_NAME,
                    "dropdown-menu dropdown-menu-right market-selector--list",
                )
            )
        )
    except Exception as inst:
        print("Scores are not available")

    totaldiv = browser.find_elements_by_class_name("close")
    expand = browser.find_element_by_id("top-expand-all")

    if len(totaldiv) > 5:
        itr = math.ceil(len(totaldiv) / 5)
        for i in range(0, itr):
            expand.click()

    else:
        expand.click()

    panels = browser.find_elements_by_class_name("panel")

    for panel in panels:
        panelTitle = panel.find_element_by_class_name("panel-title").text
        if panelTitle == title:
            try:
                WebDriverWait(browser, 5).until(
                    ExpectedConditions.element_to_be_clickable(
                        (
                            By.CLASS_NAME,
                            "dropdown",
                        )
                    )
                )
            except Exception as inst:
                print("market selector dropdowns are not available")

            dropdowns = panel.find_elements_by_class_name("dropdown")

            for dropdown in dropdowns:
                time.sleep(1)
                dropdown.click()
                options = dropdown.find_elements_by_tag_name("li")
                for option in options:
                    if dropdown1 == option.text:
                        option.click()

            pointspanel = panel.find_elements_by_class_name("offerings")
            for pointpanel in pointspanel:
                points.append(pointpanel.text)

    browser.close()

    return points