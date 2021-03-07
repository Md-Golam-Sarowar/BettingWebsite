from django.shortcuts import render
from .modules import Scapping_mybookie_ag, RandomCredentials
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def getInformationfromWebpage(request):
    scrapped_data = Scapping_mybookie_ag.getLiveSports()
    return HttpResponse("website scraped successfully")


def createrandomCredentials(request, totalCredentials):
    totalCredentials = RandomCredentials.addCredentials(totalCredentials)
    return HttpResponse("randomCredentials Saved suceessfully")


@csrf_exempt
def updateCredential(request, id):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    username = body["username"]
    password = body["password"]
    role = body["role"]
    credential = []
    credential.extend([username, password, role])
    RandomCredentials.updateCredential(credential, id)
    return HttpResponse("updated suceessfully")
