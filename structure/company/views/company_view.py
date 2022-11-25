'''
Views logic of Company 
'''

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import GenericAPIView

from structure.company.models import (
    Company,
    CompanyAssets,
    EmployeeOfCompany
)

from structure.company.serializer import (
    CompanySerialzier,
    EmployeeAssigntoCompanySerialzier
)




## Comapny API View
## Company List , Create view

class CompanyView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class =  CompanySerialzier
    queryset = Company.objects.filter(is_active=True)

    def get(self,request):
        company_obj = Company.objects.filter(is_active=True)
        company_obj_api = CompanySerialzier(company_obj,many=True)
        return Response(company_obj_api.data)
    
    def post(self,request):
        company_obj_api = CompanySerialzier(data=request.data)
        
        if company_obj_api.is_valid(raise_exception=True):
            company_obj_api.save()
            return Response(company_obj_api.data)
        else:
            return Response(company_obj_api.error_messages)
        


## Employee assign to Company API view

class AssignEmployeetoComapnyView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class =  EmployeeAssigntoCompanySerialzier
    queryset = EmployeeOfCompany.objects.filter(is_active=True)

    
    def get(self,request):

        company_employee_obj = EmployeeOfCompany.objects.filter(is_active=True)
        company_employee_obj_api = EmployeeAssigntoCompanySerialzier(company_employee_obj,many=True)

        return Response(company_employee_obj_api.data)
    
    def post(self,request):
        company_employee_obj_api = EmployeeAssigntoCompanySerialzier(data=request.data)

        if company_employee_obj_api.is_valid(raise_exception=True):
            company_employee_obj_api.save()
            return Response(company_employee_obj_api.data)
        else:
            return Response(company_employee_obj_api.error_messages)

        
## Assign Assets to Company Employee

class AssignAssetstoEmployee(GenericAPIView):
    pass 

    