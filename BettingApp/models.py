from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class userInfo(TimeStampMixin):
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    role = models.CharField(max_length=50, default="")
    available = models.IntegerField(default=0)

    def __int__(self):
        return self.id


class myBet(TimeStampMixin):
    betType = models.CharField(max_length=50, default="")
    risk = models.IntegerField(default=0)
    accept = models.IntegerField(default=0)
    sizeEnabled = models.IntegerField(default=0)
    userFreeBetId = models.IntegerField(default=0)
    a = models.CharField(max_length=100, default="")
    user = models.ForeignKey(userInfo, on_delete=models.CASCADE)

    def __int__(self):
        return self.id


class componentBet(TimeStampMixin):
    e = models.IntegerField(default=0)
    p = models.CharField(max_length=50, default="")
    m = models.IntegerField(default=0)
    k = models.IntegerField(default=0)
    v = models.IntegerField(default=0)
    sk = models.IntegerField(default=0)
    myBet = models.ForeignKey(myBet, on_delete=models.CASCADE)

    def __int__(self):
        return self.e


class betHistory(TimeStampMixin):
    ticketNo = models.IntegerField(default=0)
    win_loss_status = models.CharField(max_length=250, default="")
    win_loss_amount = models.IntegerField(default=0)
    user_phone = models.CharField(max_length=250, default="")
    win = models.IntegerField(default=0)
    risk = models.IntegerField(default=0)
    placed = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(userInfo, default=None, on_delete=models.CASCADE)
    team1 = models.CharField(max_length=250, default="")
    team2 = models.CharField(max_length=250, default="")
    whomtobet = models.CharField(max_length=250, default="")
    matchDate = models.DateTimeField(null=True)
    panelTitle = models.CharField(max_length=250, default="")
    point = models.IntegerField(default=0)
    game_point_details = models.TextField(default="")

    def __str__(self):
        return self.user_phone
