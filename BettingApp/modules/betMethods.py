from BettingApp.models import myBet, userInfo, liveSport, betHistory


def createnewBet(newBet):
    ticketNodata = newBet[0]
    user_phonedata = newBet[1]
    descriptiondata = newBet[2]
    riskvalue = newBet[3]
    winvalue = newBet[4]
    userIdvalue = newBet[5]
    userfetched = None

    try:
        userfetched = userInfo.objects.get(pk=userIdvalue)

    except Exception as ex:
        userfetched = None

    betObject = myBet(
        ticketNo=ticketNodata,
        user_phone=user_phonedata,
        description=descriptiondata,
        risk=riskvalue,
        win=winvalue,
        user=userfetched,
    )

    try:
        betObject.save()
    except Exception as ex:
        return False

    return True


def deleteBet(betId):
    print("deleted successfully")
