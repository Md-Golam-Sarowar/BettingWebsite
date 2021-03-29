from BettingApp.models import myBet, userInfo, betHistory, componentBet
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from bs4 import BeautifulSoup


def createnewBet(newBet):

    betObject = myBet(
        eventId=newBet[0],
        classifier=newBet[1],
        groupName=newBet[2],
        label=newBet[3],
        line=newBet[4],
        marketId=newBet[5],
        marketName=newBet[6],
        oddsName=newBet[7],
        oddsVal=newBet[8],
        toWin=newBet[9],
        betType=newBet[10],
        risk=newBet[11],
        accept=newBet[12],
        sizeEnabled=newBet[13],
        userFreeBetId=newBet[14],
        a=newBet[15],
        user=newBet[16],
        ticketno=newBet[18],
        teamname=newBet[19],
    )

    betObject.save()
    createdBetId = betObject.id

    componentBets = newBet[17]

    for bet in componentBets:
        componentobj = componentBet(
            e=bet["e"],
            p=bet["p"],
            m=bet["m"],
            k=bet["k"],
            v=bet["v"],
            myBet=betObject,
        )
        componentobj.save()

    return betObject


def deleteBet(betId):
    print("deleted successfully")
