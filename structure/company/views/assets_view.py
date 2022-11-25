'''
Views logic of Company  assets 
'''

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import GenericAPIView

from structure.company.models import (
    CompanyAssets,

)

from structure.company.serializer import (
    CompanyAssetsSerializer
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
        return Response(company_assets_obj_api.data)
    
    def post(self,request):
        company_assets_obj_api = CompanyAssetsSerializer(data=request.data)
        
        if company_assets_obj_api.is_valid(raise_exception=True):
            company_assets_obj_api.save()
            return Response(company_assets_obj_api.data)
        else:
            return Response(company_assets_obj_api.error_messages)
