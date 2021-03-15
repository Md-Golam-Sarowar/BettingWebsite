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
    ticketNo = models.IntegerField(default=0)
    user_phone = models.CharField(max_length=250)
    description = models.TextField()
    win = models.IntegerField(default=0)
    risk = models.IntegerField(default=0)
    placed = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(userInfo, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_phone


class betHistory(TimeStampMixin):
    ticketNo = models.IntegerField(default=0)
    user_phone = models.CharField(max_length=250)
    description = models.TextField()
    win = models.IntegerField(default=0)
    risk = models.IntegerField(default=0)
    placed = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(userInfo, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_phone
