# python -m pip install virtualenvwrapper-win
# mkvirtualenv sports
# pip install django
# django-admin --version
# django-admin startproject SportsWebsite
# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate

"""SportsWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BettingApp.views import (
    getLeagueInformation,
    homePage,
    getfromwebpageslower,
    getdropdownoptions,
    createrandomCredentials,
    updateCredential,
    readCredentials,
    deleteCredential,
    index,
    findCredential,
    createBet,
    deleteBet,
    readBets,
    authenticate,
    logout,
    showHistory,
    userInformation,
    OpenBets,
    betHistorydetails,
    adminaccess,
    showsports,
    parl,
    teaser,
    createSports,
    getteaserlist,
    allActiveBets,
    scappingwebLeagueInfo,
    checkedLeaguesInformation,
    scappingLeagueInfoforContinueButton,
    TeaserSports,
    scappingLeagueInfoforTeacher,
)

urlpatterns = [
    path("", index),
    path("createSports", createSports),
    path("teaserlist", getteaserlist),
    path("home", homePage),
    path("adminAccess", adminaccess),
    path("vipLiveBetting", homePage),
    path("openBets", OpenBets),
    path("betHistory", betHistorydetails),
    path("login", authenticate),
    path("logout", logout),
    path("userinformation", userInformation),
    path("leagueInformation/<str:name>", getLeagueInformation),
    path("teaserSports/<str:ids>", TeaserSports),
    path("checkedLeagues/<str:listofNames>", checkedLeaguesInformation),
    path("slowerscrapping", getfromwebpageslower),
    path("dropdownoptions", getdropdownoptions),
    path("generatecredentials/<int:totalCredentials>", createrandomCredentials),
    path("dashboard", readCredentials),
    path("updateCredential/<int:id>", updateCredential),
    path("deleteCredential/<int:id>", deleteCredential),
    path("findCredential/<int:id>", findCredential),
    path("createBet", createBet),
    path("deleteBet/<int:betId>", deleteBet),
    path("readBets/<int:userId>", readBets),
    path("showHistory/<int:userId>", showHistory),
    path("sports", showsports),
    path("parlay", parl),
    path("teaser", teaser),
    path("ActiveBets", allActiveBets),
    path("scappingLeagueInfo", scappingwebLeagueInfo),
    path("scappingLeagueInfoforContinue", scappingLeagueInfoforContinueButton),
    path("scappingLeagueInfoforTeacher", scappingLeagueInfoforTeacher),
]
