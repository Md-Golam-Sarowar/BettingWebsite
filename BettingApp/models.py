from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class userInfo(TimeStampMixin):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    available = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class liveSport(TimeStampMixin):
    name = models.CharField(max_length=250)
    team1 = models.CharField(max_length=250)
    team2 = models.CharField(max_length=250)
    dateTime = models.CharField(max_length=250)
    live = models.CharField(max_length=250)
    point1 = models.CharField(max_length=250)
    point2 = models.CharField(max_length=250)
    point3 = models.CharField(max_length=250)
    point4 = models.CharField(max_length=250)
    point5 = models.CharField(max_length=250)
    point6 = models.CharField(max_length=250)
    liveInfo = models.CharField(max_length=250)
    score1 = models.CharField(max_length=250)
    score2 = models.CharField(max_length=250)
    sportCategory = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class myBet(TimeStampMixin):
    risk = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    user = models.ForeignKey(userInfo, default=None, on_delete=models.DO_NOTHING)
    sport = models.ForeignKey(liveSport, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user


class betHistory(TimeStampMixin):
    mybet = models.ForeignKey(myBet, default=None, on_delete=models.DO_NOTHING)
    win_lose = models.CharField(max_length=250)
    balance = models.IntegerField(default=0)
    user = models.ForeignKey(userInfo, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.win_lose
