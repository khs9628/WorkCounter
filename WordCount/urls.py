from django.urls import path

from .views import *
from . import views

app_name = "WordCount"

urlpatterns=[
    path('', MainpageView.as_view(), name='mainpage'),
    path('home/', views.home, name='home'), #name은 url의 이름을 설정한다.
    path('about/', views.about, name='about'),
    path('result/', views.result, name='result'),
]