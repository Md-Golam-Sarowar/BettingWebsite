import random
import string
from BettingApp.models import userInfo
from django.shortcuts import get_object_or_404


def addCredentials(totalCredentials):

    userInfo.objects.all().delete()
    credentials = []

    for i in range(0, totalCredentials):
        usernameRandom = "".join(random.choice(string.ascii_letters) for i in range(10))
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(password_characters) for i in range(8))
        role = "user"
        availablepoint = 1000
        credentialObject = userInfo(
            username=usernameRandom,
            password=password,
            role=role,
            available=availablepoint,
        )
        credentialObject.save()
        credentials.append(usernameRandom)
        credentials.append(password)
        credentials.append(role)

    return credentials


def updateCredential(updatecredential, id):
    credential = userInfo.objects.get(pk=id)
    credential.username = updatecredential[0]
    credential.password = updatecredential[1]
    credential.role = updatecredential[2]
    credential.save()


def deleteCredential(id):
    credential = userInfo.objects.get(pk=id)
    credential.delete()


def findCredential(id):
    try:
        credential = userInfo.objects.get(pk=id)
    except Exception as inst:
        credential = None
    return credential


def readCredentials():
    allCredentials = userInfo.objects.all()
    return allCredentials
