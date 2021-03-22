from BettingApp.models import myBet, userInfo, betHistory, componentBet


def createnewBet(newBet):

    betObject = myBet(
        betType=newBet[0],
        risk=newBet[1],
        accept=newBet[2],
        sizeEnabled=newBet[3],
        userFreeBetId=newBet[4],
        a=newBet[5],
        user=newBet[6],
    )

    betObject.save()
    createdBetId = betObject.id

    componentBets = newBet[7]

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


def deleteBet(betId):
    print("deleted successfully")
