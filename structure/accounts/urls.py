# accounts URL config 

from django.urls import path 
from structure.accounts.views import (
    RegisterAPIView
)


urlpatterns = [
    path('register/',RegisterAPIView.as_view(),name='register')

]



