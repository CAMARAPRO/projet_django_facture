from django.urls import path
from fac_app.views import *

urlpatterns = [
    path('',home, name='home')
]
