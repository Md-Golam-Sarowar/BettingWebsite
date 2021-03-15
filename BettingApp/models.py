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

    def __str__(self):
        return self.username


class liveSport(TimeStampMixin):
    name = models.CharField(max_length=250, default="")
    team1 = models.CharField(max_length=250, default="")
    team2 = models.CharField(max_length=250, default="")
    dateTime = models.CharField(max_length=250, default="")
    live = models.CharField(max_length=250, default="")
    point1 = models.CharField(max_length=250, default="")
    point2 = models.CharField(max_length=250, default="")
    point3 = models.CharField(max_length=250, default="")
    point4 = models.CharField(max_length=250, default="")
    point5 = models.CharField(max_length=250, default="")
    point6 = models.CharField(max_length=250, default="")
    liveInfo = models.CharField(max_length=250, default="")
    score1 = models.CharField(max_length=250, default="")
    score2 = models.CharField(max_length=250, default="")
    sportCategory = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.name


class myBet(TimeStampMixin):
    ticketNo = models.IntegerField(default=0)
    user_phone = models.CharField(max_length=250, default="")
    win = models.IntegerField(default=0)
    risk = models.IntegerField(default=0)
    placed = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(userInfo, default=None, on_delete=models.CASCADE)
    team1 = models.CharField(max_length=250, default="")
    team2 = models.CharField(max_length=250, default="")
    whomtobet = models.CharField(max_length=260, default="")
    matchDate = models.DateTimeField(null=True)
    panelTitle = models.CharField(max_length=250, default="")
    point = models.IntegerField(default=0)
    game_point_details = models.TextField(default="")  # Game / Total: Over 206.5  -117

    def __str__(self):
        return self.user_phone


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
