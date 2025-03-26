from django.urls import path
from .views import *

app_name='wordcount'

urlpatterns = [
    path('',index, name='index'),
    path('word-count/',word_count,name='word_count'),
    path('result/',result, name='result'),
    path('hello/',hello, name='hello'),
]

