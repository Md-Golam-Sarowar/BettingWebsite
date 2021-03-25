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
from .models import myBet, userInfo, betHistory, componentBet
import json
from django.http import JsonResponse
from SportsWebsite.settings import BASE_DIR, settings_dir, PROJECT_ROOT


# Create your views here.
def index(request):
    return render(request, "Welcome to BetBig247.com.html")


def betHistorydetails(request):
    userfetched = userInfo.objects.get(id=request.session["id"])
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
    return render(request, "betHistory.html", data)


def OpenBets(request):
    userfetched = userInfo.objects.get(id=request.session["id"])
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
    return render(request, "myBets.html", data)


def createSports(request):

    userfetched = userInfo.objects.get(id=request.session["id"])
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
    return render(request, "createSports.html", data)


def getteaserlist(request):
    return render(request, "getteaserlist.html")


def homePage(request):

    userfetched = userInfo.objects.get(id=request.session["id"])
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


def userInformation(request):
    userfetched = userInfo.objects.get(id=request.session["id"])
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

    return JsonResponse(
        data,
        content_type="application/json",
    )


def readCredentials(request):
    allCredentials = RandomCredentials.readCredentials()
    userIds = []
    usernames = []
    passwords = []
    roles = []
    credentials = []
    admin = []
    for data in allCredentials:
        singleCredential = dict()

        if data.role != "admin":
            singleCredential["id"] = data.id
            singleCredential["username"] = data.username
            singleCredential["password"] = data.password
            singleCredential["role"] = data.role
            credentials.append(singleCredential)
        elif data.role == "admin":
            singleCredential["id"] = data.id
            singleCredential["username"] = data.username
            singleCredential["password"] = data.password
            singleCredential["role"] = data.role
            admin.append(singleCredential)

    return render(request, "index3.html", {"credentials": credentials, "admin": admin})


def adminaccess(request):
    if request.session.get("username") and request.session.get("role") == "admin":
        data = {
            "loggedin": "yes",
            "role": "admin",
        }
    elif request.session.get("username"):
        data = {
            "loggedin": "yes",
            "role": "user",
        }

    return JsonResponse(
        {
            "status": 200,
            "data": data,
            "base_dir": "http://" + request.META["HTTP_HOST"],
        },
        content_type="application/json",
    )


@csrf_exempt
def updateCredential(request, id):
    username = request.POST["username"]
    password = request.POST["password"]
    role = request.POST["role"]
    credential = []
    credential.extend([username, password, role])
    RandomCredentials.updateCredential(credential, id)
    return JsonResponse(
        {
            "status": 200,
            "base_dir": "http://" + request.META["HTTP_HOST"],
        },
        content_type="application/json",
    )


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
    body = json.loads(request.body)
    eventId = body["eventId"]
    classifier = body["classifier"]
    groupName = body["groupName"]
    label = body["label"]
    line = body["line"]
    marketId = body["marketId"]
    marketName = body["marketName"]
    oddsName = body["oddsName"]
    oddsVal = body["oddsVal"]
    toWin = body["toWin"]
    betType = body["type"]
    risk = body["risk"]
    accept = body["accept"]
    sizesenabled = body["sizesEnabled"]
    userFreeBetId = body["userFreeBetId"]
    components = body["componentBets"]
    a = body["a"]

    fetchedUser = userInfo.objects.filter(id=request.session["id"])
    user = fetchedUser[0]

    userfetched = userInfo.objects.get(id=request.session["id"])
    allBets = myBet.objects.filter(user=userfetched)

    riskValueDb = 0
    for bet in allBets:
        riskValueDb = riskValueDb + bet.risk

    newBet = []

    newBet.extend(
        [
            eventId,
            classifier,
            groupName,
            label,
            line,
            marketId,
            marketName,
            oddsName,
            oddsVal,
            toWin,
            betType,
            risk,
            accept,
            sizesenabled,
            userFreeBetId,
            a,
            user,
            components,
        ]
    )

    if (riskValueDb + risk) > user.available or (riskValueDb + risk) > 300:
        return JsonResponse(
            {
                "Failed": "risk value exceeds user limit! ",
                "status": 500,
            },
            content_type="application/json",
        )
    else:
        createdBet = betMethods.createnewBet(newBet)
        print(createdBet)
        return JsonResponse(
            {
                "success": "successfully creatednewBet",
                "status": 200,
            },
            content_type="application/json",
        )


def readBets(request, userId):
    userfetched = userInfo.objects.get(id=userId)
    allBets = myBet.objects.filter(user=userfetched)
    for bet in allBets:
        print(bet.id, bet.risk, bet.user.id, bet.userFreeBetId)
    return HttpResponse("bets Read suceessfully")


def deleteBet(request, betId):
    betMethods.deleteBet(betId)
    return HttpResponse("deleted successfully")


def deleteCredential(request, id):
    RandomCredentials.deleteCredential(id)
    return JsonResponse(
        {
            "status": 200,
        },
        content_type="application/json",
    )


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
    return JsonResponse(
        {
            "status": 200,
            "base_dir": "http://" + request.META["HTTP_HOST"],
        },
        content_type="application/json",
    )


def showsports(request):
    userfetched = userInfo.objects.get(id=request.session["id"])
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
    return render(request, "showSports.html", data)


def parl(request):
    userfetched = userInfo.objects.get(id=request.session["id"])
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
    return render(request, "parl.html", data)


def teaser(request):
    userfetched = userInfo.objects.get(id=request.session["id"])
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
    return render(request, "teaser.html", data)


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
        request.session["id"] = user.id
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
