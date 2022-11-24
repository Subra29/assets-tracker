# accounts URL config 

from django.urls import path 
from structure.accounts.views import (
    LoginView,
    RegisterView,
    LogoutView,
    CheckPhoneNumber
)


urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path('sign-up/',RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout')

]

hx_response_url = [
    path('check/phone/number/',CheckPhoneNumber.as_view(),name="check_phone"),
]

urlpatterns += hx_response_url


