from django.urls import path
from calculator.views import *
urlpatterns = [
    path('',index,name='index')
]