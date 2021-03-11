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

featured = []
Basketball = []
College_basketball = []
Hockey = []
Soccer = []
Tennis = []
Cricket = []
Volleyball = []
Football = []
MMA = []
Baseball = []


def processingpanelInfo(panel):
    panelInfo = dict()
    panelInfo["panelTitle"] = panel.find("h3", class_="panel-title").text
    panelInfo["eventlistheader"] = panel.find("div", class_="event-list__header").text
    events = panel.find_all("div", class_="event-list__item")
    itr = 0
    for event in events:
        panelInfonew = dict()
        itr = itr + 1
        eventindex = "event" + str(itr)
        panelInfonew["timeliveSportinfo"] = event.find(
            "div", class_="event-list__item__details__date"
        ).text
        teams = event.find_all("p", class_="event-list__item__details__teams__team")
        panelInfonew["team1"] = teams[0].text
        panelInfonew["team2"] = teams[1].text
        scores = event.find_all("div", class_="event-scores__team-period")
        if scores != None:
            i = 0
            for score in scores:
                i = i + 1
                index = "score" + str(i)
                panelInfonew[index] = score.text
        oddlinks = event.find_all("div", class_="odd link")

        if oddlinks != None:
            j = 0
            for oddlink in oddlinks:
                j = j + 1
                index = "oddlink" + str(j)
                panelInfonew[index] = oddlink.text

        detailsmoreinfo = event.find("div", class_="event-list__item__details__more")
        panelInfonew["detailsmore"] = detailsmoreinfo.text
        panelInfo[eventindex] = panelInfonew

    print(panelInfo, "\n\n")
    return panelInfo


def liveSports():
    validSports = [
        "Tennis",
        "Football",
        "Basketball",
        "Volleyball",
        "MMA",
        "Baseball",
        "Soccer",
        "College Basketball",
        "Cricket",
        "Hockey",
        "Featured",
    ]
    url = "https://plive.dgs.phnserv.eu/live/?#!/home"
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")

    browser = webdriver.Chrome(options=options)

    browser.get(url)

    try:
        WebDriverWait(browser, 15).until(
            ExpectedConditions.element_to_be_clickable(
                (By.CLASS_NAME, "sports-menu__item-link")
            )
        )
    except Exception as inst:
        print("sportMenu not found")

    sportsMenu = BeautifulSoup(browser.page_source, "html.parser").find_all(
        "ul", class_="sports-menu"
    )

    baseUrl = "https://plive.dgs.phnserv.eu/live/?"

    for sport in sportsMenu[0]:
        name = sport.find("a", class_="sports-menu__item-link").text
        href = sport.find("a", class_="sports-menu__item-link").get("href")
        liveUrl = baseUrl + href

        browser.get(liveUrl)

        totaldiv = browser.find_elements_by_class_name("close")
        expand = browser.find_element_by_id("top-expand-all")

        if len(totaldiv) > 5:
            itr = math.ceil(len(totaldiv) / 5)
            for i in range(0, itr):
                expand.click()

        else:
            expand.click()

        namestripped = "".join([i for i in name if not i.isdigit()])

        if namestripped in validSports:
            print(namestripped)
            try:
                WebDriverWait(browser, 10).until(
                    ExpectedConditions.presence_of_element_located(
                        (By.CLASS_NAME, "event-scores__team-period")
                    )
                )
            except Exception as inst:
                print("Scores are not available")

            except Exception as inst:
                print("Golf or others Scores are not available")

        panelperSportName = BeautifulSoup(browser.page_source, "html.parser").find_all(
            "div", class_="panel"
        )

        for panel in panelperSportName:
            if "Featured" in name:
                panelInfo = processingpanelInfo(panel)
                featured.append(panelInfo)
            elif "Tennis" in name:
                panelInfo = processingpanelInfo(panel)
                Tennis.append(panelInfo)
            elif "Basketball" in name:
                panelInfo = processingpanelInfo(panel)
                Basketball.append(panelInfo)
            elif "Volleyball" in name:
                panelInfo = processingpanelInfo(panel)
                Volleyball.append(panelInfo)
            elif "Soccer" in name:
                panelInfo = processingpanelInfo(panel)
                Soccer.append(panelInfo)
            elif "Hockey" in name:
                panelInfo = processingpanelInfo(panel)
                Hockey.append(panelInfo)
            elif "Cricket" in name:
                panelInfo = processingpanelInfo(panel)
                Cricket.append(panelInfo)
            elif "Football" in name:
                panelInfo = processingpanelInfo(panel)
                Football.append(panelInfo)
            elif "Baseball" in name:
                panelInfo = processingpanelInfo(panel)
                Baseball.append(panelInfo)
            elif "MMA" in name:
                panelInfo = processingpanelInfo(panel)
                MMA.append(panelInfo)
            elif "College Basketball" in name:
                panelInfo = processingpanelInfo(panel)
                College_basketball.append(panelInfo)


liveSports()