from django.urls import path
from .views import *

app_name = 'phone'

urlpatterns = [
    path('', list, name = 'list'),
    path('result/', result, name = 'result'),
]
