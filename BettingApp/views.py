from django.shortcuts import render
from .modules import (
    fasterScrappingLive,
    RandomCredentials,
    betMethods,
    slowerScrappingLivewithDropdown,
    dropdownpoints,
)
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def index(request):
    return render(request, "Welcome to BetBig247.com.html")


def homePage(request):
    return render(request, "Betting Site.html")


def readCredentials(request):
    allCredentials = RandomCredentials.readCredentials()
    return HttpResponse("credentials read successfully")


@csrf_exempt
def updateCredential(request, id):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    username = body["username"]
    password = body["password"]
    role = body["role"]
    credential = []
    credential.extend([username, password, role])
    RandomCredentials.updateCredential(credential, id)
    return HttpResponse("updated suceessfully")


def findCredential(request, id):
    credential = RandomCredentials.findCredential(id)
    if credential:
        print(credential)
        return HttpResponse("found suceessfully")
    else:
        print("Not found")
        return HttpResponse("not found")


@csrf_exempt
def createBet(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    risk = body["risk"]
    userId = body["userId"]
    sportId = body["sportId"]
    newBet = []
    newBet.extend([risk, userId, sportId])
    betMethods.createnewBet(newBet)
    return HttpResponse("created suceessfully")


def deleteCredential(request, id):
    RandomCredentials.updateCredential(id)
    return HttpResponse("deleted suceessfully")


def getfromwebpagesfaster(request):
    scrapped_data = fasterScrappingLive.liveSports()
    print(scrapped_data)
    return HttpResponse("website fasterscraped successfully")


def getfromwebpageslower(request):
    scrapped_data = slowerScrappingLivewithDropdown.liveSports()
    print(scrapped_data)
    return HttpResponse("website slowerscraped successfully")


def getdropdownoptions(request):
    dropdownmenus = dropdownpoints.dropdowninfo()
    print(dropdownmenus)
    return HttpResponse("dropdownmenus extracted successfully")


def createrandomCredentials(request, totalCredentials):
    totalCredentials = RandomCredentials.addCredentials(totalCredentials)
    return HttpResponse("randomCredentials Saved suceessfully")
