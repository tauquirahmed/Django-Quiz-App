from django.contrib import admin
from django.urls import path
from home.views import *


urlpatterns = [
    path('', home, name = "home"),
    path('api/get-quiz/', get_quiz, name = 'get_quiz'),
    path('quiz/', quiz, name="quiz")
]
