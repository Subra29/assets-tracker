# Company URL config 

from django.urls import path 
from structure.company.views.company_view import (
    CompanyView,
    AssignEmployeetoComapnyView
)
from structure.company.views.assets_view import (
    CompanyAssetsView
)

urlpatterns = [
    path('',CompanyView.as_view()),
    path('add/employee/',AssignEmployeetoComapnyView.as_view()),
    path('assets/',CompanyAssetsView.as_view())
]
