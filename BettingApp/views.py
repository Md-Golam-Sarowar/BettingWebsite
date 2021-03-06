from django.shortcuts import render
from .modules import Scapping_mybookie_ag, RandomCredentials
from django.http import HttpResponse

# Create your views here.


def getInformationfromWebpage(request):
    scrapped_data = Scapping_mybookie_ag.getLiveSports()
    return HttpResponse("website scraped successfully")


def createrandomCredentials(request, totalCredentials):
    totalCredentials = RandomCredentials.addCredentials(totalCredentials)
    return HttpResponse("randomCredentials Saved suceessfully")


def updateCredential(request, id):
    username = request.POST["username"]
    password = request.POST["password"]
    role = request.POST["role"]
    credential = []
    credential.extend([username, password, role])
    RandomCredentials.updateCredential(credential, id)
