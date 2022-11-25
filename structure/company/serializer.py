'''
Seralizer of Company 
'''

from rest_framework import serializers

from structure.accounts.models.employee import Employee
from structure.company.models import (
    Company,
    CompanyAssets,
    EmployeeOfCompany,
    DeligateAssetstoEmployee
)


## Company Serializer 

class CompanySerialzier(serializers.ModelSerializer):
    
    admin = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    admin_name = serializers.CharField(source='admin.full_name',read_only=True)
    
    class Meta:
        model = Company
        fields = [
            'id',
            'admin_name',
            'admin',
            'name',
            'info',
        ]

        
## Employee Assign to Company Serializer 

class EmployeeAssigntoCompanySerialzier(serializers.ModelSerializer):
    
    company_name = serializers.CharField(source='company.name',read_only=True)
    employee_name = serializers.CharField(source='employee.full_name',read_only=True)

    class Meta:
        model = EmployeeOfCompany
        fields = [
            'id',
            'company_name',
            'company',
            'employee_name',
            'employee'
        ]

    ## Override Create method to check 
        # if an Employee already in a company 
        # if not then save the instance 

    def create(self,validated_data):

        employee = validated_data.pop('employee')
        company  = validated_data.pop('company')

        if EmployeeOfCompany.objects.filter(
            company=company,
            employee=employee
        ).exists():
            
            raise serializers.ValidationError("Employee Already Added")
        else:
            employee_obj = EmployeeOfCompany(
                company=company,
                employee=employee
            )
            employee_obj.save()
            return employee_obj

          
## Company Asset Serialzier 
        
class CompanyAssetsSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source='company.name',read_only=True)

    class Meta:
        model = CompanyAssets
        fields = [
            'id',
            'company_name',
            'company',
            'device_name',
            'device_type'
        ]

        
## Assets assign to Employee Serializer 
        
class AssignAssetToEmployeeSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source='asset.company.name',read_only=True)
    asset_name = serializers.CharField(source='asset.device_name',read_only=True)
    employee_name = serializers.CharField(source='employee',read_only=True)

    class Meta:
        model = DeligateAssetstoEmployee
        fields = [
            'id',
            'company_name',
            'asset_name',
            'asset',
            'employee_name',
            'employee',
            'checking_out_date',
            'checking_out_condition_log',
            'return_date',
            'return_condition_log'
        ]


## Device log API seralizer 
# Nested API 
        
class DeviceUsesSerializer(serializers.ModelSerializer):

    employee_id = serializers.CharField(source='employee.id',read_only=True)
    employee_name = serializers.CharField(source='employee.full_name',read_only=True)

    class Meta:
        model = DeligateAssetstoEmployee
        fields = [
            'id',
            'employee_id',
            'employee_name',
            'checking_out_date',
            'checking_out_condition_log',
            'return_date',
            'return_condition_log'
        ]
   

class DeviceLogSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source='company.name',read_only=True)
    assigned_assets = DeviceUsesSerializer(many=True)

    class Meta:
        model = CompanyAssets
        fields = [
            'id',
            'company_name',
            'device_name',
            'device_type',
            'assigned_assets'
        ]