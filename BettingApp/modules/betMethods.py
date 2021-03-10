from BettingApp.models import myBet, userInfo, liveSport, betHistory


def createnewBet(newBet):
    risk = newBet[0]
    userId = newBet[1]
    sportId = newBet[2]

    try:
        userfetched = userInfo.objects.get(pk=userId)
        sport = liveSport.objects.get(pk=sportId)
        allHistory = betHistory.objects.get(user.id == userfetched.id).order_by(
            betHistory.id
        )
    except Exception as ex:
        userfetched = None
        sport = None
        allHistory = None
    print(userfetched, sport, allHistory)