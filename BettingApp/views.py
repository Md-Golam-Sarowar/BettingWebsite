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
from .models import myBet, userInfo, myBet, betHistory
import json
from django.http import JsonResponse
from SportsWebsite.settings import BASE_DIR, settings_dir, PROJECT_ROOT


# Create your views here.
def index(request):
    return render(request, "Welcome to BetBig247.com.html")


def homePage(request):

    userfetched = userInfo.objects.get(username=request.session["username"])
    allBets = myBet.objects.filter(user=userfetched)
    allBetsHistory = betHistory.objects.filter(user=userfetched)

    risk = 0
    for bet in allBets:
        risk = risk + bet.risk

    balance = 0
    for bethistory in allBetsHistory:
        balance = balance + betHistory.win_loss_amount

    data = {
        "username": request.session["username"],
        "password": request.session["password"],
        "available": request.session["available"],
        "risk": risk,
        "balance": balance,
    }
    return render(request, "Betting Site.html", data)


def readCredentials(request):
    allCredentials = RandomCredentials.readCredentials()
    for data in allCredentials:
        print(
            data.id,
            "  ",
            data.username,
            "  ",
            data.password,
        )
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
    ticketNo = body["ticketNo"]
    user_phone = body["user_phone"]
    placed = body["placed"]
    risk = body["risk"]
    win = body["win"]
    user = body["userId"]
    team1 = body["team1"]
    team2 = body["team2"]
    whomtobet = body["whomtobet"]
    matchDate = body["matchDate"]
    panelTitle = body["panelTitle"]
    game_point_details = body["game_point_details"]
    point = body["point"]
    newBet = []
    newBet.extend(
        [
            ticketNo,
            user_phone,
            placed,
            risk,
            win,
            user,
            team1,
            team2,
            whomtobet,
            matchDate,
            panelTitle,
            game_point_details,
            point,
        ]
    )
    createdBet = betMethods.createnewBet(newBet)

    if createdBet == True:
        return HttpResponse("created suceessfully")
    else:
        return HttpResponse("failed to create")


def readBets(request, userId):
    userfetched = userInfo.objects.get(id=userId)
    allBets = myBet.objects.filter(user=userfetched)
    for bet in allBets:
        print(bet.risk)
    return HttpResponse("bets Read suceessfully")


def deleteBet(request, betId):
    betMethods.deleteBet(betId)
    return HttpResponse("deleted successfully")


def deleteCredential(request, id):
    RandomCredentials.deleteCredential(id)
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


@csrf_exempt
def authenticate(request):
    usernamedata = request.POST["username"]
    passworddata = request.POST["password"]
    flag = False
    user = None

    allData = userInfo.objects.all()

    for data in allData:
        if data.username == usernamedata and data.password == passworddata:
            flag = True
            user = data
            break

    if flag == True:
        request.session["username"] = user.username
        request.session["password"] = user.password
        request.session["role"] = user.role
        request.session["available"] = user.available
        return JsonResponse(
            {
                "success": "successfully authenticated",
                "status": 200,
                "base_dir": "http://" + request.META["HTTP_HOST"],
            },
            content_type="application/json",
        )
    else:
        return JsonResponse(
            {"error": "failed to authenticate", "status": 500},
            content_type="application/json",
        )


def logout(request):
    request.session.flush()
    return JsonResponse(
        {
            "success": "successfully logged out",
            "status": 200,
        },
        content_type="application/json",
    )


def showHistory(request, userId):
    return HttpResponse("showed all the history for " + str(userId))
