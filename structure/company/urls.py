# Company URL config 

from django.urls import path 
from structure.company.views.company_view import (
    CompanyView,
    AssignEmployeetoComapnyView
)
from structure.company.views.assets_view import (
    CompanyAssetsView,
    AssignAssetstoEmployeeView,
    SingleAssignAssetstoEmployeeView,
    DeviceLogView
)

urlpatterns = [
    path('',CompanyView.as_view()),
    path('add/employee/',AssignEmployeetoComapnyView.as_view()),
    path('assets/',CompanyAssetsView.as_view()),
    path('assign/assets/',AssignAssetstoEmployeeView.as_view()),
    path('assign/assets/<uuid:pk>/',SingleAssignAssetstoEmployeeView.as_view()),
    path('assets/log/',DeviceLogView.as_view())
]
