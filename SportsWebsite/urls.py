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
    getfromwebpagesfaster,
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
    # updateBet,
    # deleteBet,
    # readBets,
)

urlpatterns = [
    path("", index),
    path("home", homePage),
    path("fasterscrapping", getfromwebpagesfaster),
    path("slowerscrapping", getfromwebpageslower),
    path("dropdownoptions", getdropdownoptions),
    path("generatecredentials/<int:totalCredentials>", createrandomCredentials),
    path("readcredentials", readCredentials),
    path("update/<int:id>", updateCredential),
    path("delete/<int:id>", deleteCredential),
    path("findCredential/<int:id>", findCredential),
    path("createBet", createBet),
    # path("updateBet", updateBet),
    # path("deleteBet", deleteBet),
    # path("readBets", readBets),
]
