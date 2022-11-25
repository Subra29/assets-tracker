'''
Seralizer of Company 
'''

from rest_framework import serializers

from structure.accounts.models.employee import Employee
from structure.company.models import (
    Company,
    CompanyAssets,
    EmployeeOfCompany
)


class CompanySerialzier(serializers.ModelSerializer):
    
    admin = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    class Meta:
        model = Company
        fields = [
            'id',
            'admin',
            'name',
            'info',
        ]

class EmployeeAssigntoCompanySerialzier(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeOfCompany
        fields = [
            'id',
            'company',
            'employee'
        ]

# class AssignAssetToEmployee(serializers.ModelSerializer):

#     class Meta:
#         model = AssignAssetToEmployee
        

class CompanyAssetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyAssets
        fields = [
            'id',
            'company',
            'device_name',
            'device_type'
        ]