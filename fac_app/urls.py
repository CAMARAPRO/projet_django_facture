from django.urls import path
from fac_app.views import *

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('add-customer', AddCustomerView.as_view(), name='add-customer')
]
