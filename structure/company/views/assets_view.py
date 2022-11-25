'''
Views logic of Company  assets 
'''

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import GenericAPIView

from structure.company.models import (
    CompanyAssets,
    DeligateAssetstoEmployee

)

from structure.company.serializer import (
    CompanyAssetsSerializer,
    AssignAssetToEmployeeSerializer,
    DeviceLogSerializer
)


## Company Assets View

class CompanyAssetsView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class =  CompanyAssetsSerializer
    queryset = CompanyAssets.objects.filter(is_active=True)

    def get(self,request):
        company_assets_obj = CompanyAssets.objects.filter(is_active=True)
        company_assets_obj_api = CompanyAssetsSerializer(company_assets_obj,many=True)
        return Response(company_assets_obj_api.data,
            status=status.HTTP_200_OK)
    
    def post(self,request):
        company_assets_obj_api = CompanyAssetsSerializer(data=request.data)
        
        if company_assets_obj_api.is_valid(raise_exception=True):
            company_assets_obj_api.save()
            return Response(company_assets_obj_api.data,
                status.HTTP_201_CREATED)
        else:
            return Response(company_assets_obj_api.error_messages,
                status=status.HTTP_406_NOT_ACCEPTABLE)


## Assign Assets to Company Employee

class AssignAssetstoEmployeeView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class =  AssignAssetToEmployeeSerializer
    queryset = DeligateAssetstoEmployee.objects.filter(is_active=True)

    def get(self,request):
        
        asset_to_employee_obj = DeligateAssetstoEmployee.objects.filter(is_active=True)
        asset_to_employee_obj_api = AssignAssetToEmployeeSerializer(asset_to_employee_obj,many=True)

        return Response(asset_to_employee_obj_api.data,
            status=status.HTTP_200_OK)
    
    def post(self,request):
        asset_to_employee_obj_api = AssignAssetToEmployeeSerializer(data=request.data)

        if asset_to_employee_obj_api.is_valid(raise_exception=True):
            asset_to_employee_obj_api.save()
            return Response(asset_to_employee_obj_api.data,
                status=status.HTTP_201_CREATED)
        else:
            return Response(asset_to_employee_obj_api.error_messages,
                status=status.HTTP_406_NOT_ACCEPTABLE)
        


class SingleAssignAssetstoEmployeeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class =  AssignAssetToEmployeeSerializer
    queryset = DeligateAssetstoEmployee.objects.filter(is_active=True)



class DeviceLogView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class =  DeviceLogSerializer
    queryset = CompanyAssets.objects.filter(is_active=True)