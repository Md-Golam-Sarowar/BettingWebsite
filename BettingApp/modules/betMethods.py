from BettingApp.models import myBet, userInfo, liveSport, betHistory


def createnewBet(newBet):
    userfetched = None

    try:
        userfetched = userInfo.objects.get(pk=newBet[5])

    except Exception as ex:
        userfetched = None

    betObject = myBet(
        ticketNo=newBet[0],
        user_phone=newBet[1],
        placed=newBet[2],
        risk=newBet[3],
        win=newBet[4],
        user=userfetched,
        team1=newBet[6],
        team2=newBet[7],
        whomtobet=newBet[8],
        matchDate=newBet[9],
        panelTitle=newBet[10],
        game_point_details=newBet[11],
        point=newBet[12],
    )

    try:
        betObject.save()
    except Exception as ex:
        print(ex)
        return False

    return True


def deleteBet(betId):
    print("deleted successfully")
