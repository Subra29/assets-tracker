import uuid
from django.db import models
from mainConfig.models.mixin import TimeStampMixin


## Company Database model 

class Company(TimeStampMixin):

    admin = models.ForeignKey(
        "accounts.Employee",on_delete=models.CASCADE,null=True,
        related_name = "company_admin"
    )
    name = models.CharField(
        max_length=200, null=True
    )
    info = models.TextField(blank=True)
    employees = models.ManyToManyField(
        'accounts.Employee',related_name='employees',
        through='EmployeeOfCompany'
    )


    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Company"

    
## Employee of Company 

class EmployeeOfCompany(TimeStampMixin):

    company = models.ForeignKey(
        "company.Company",on_delete=models.CASCADE,null=True,
        related_name = "company"
    )
    employee = models.ForeignKey(
        "accounts.Employee",on_delete=models.CASCADE,null=True,
        related_name = "employee"
    )
    

    def __str__(self):
        return f"Company : {self.company} | Employee : {self.employee}"

    class Meta:
        verbose_name_plural = "Employee of Company List"


## Company Assets 

class CompanyAssets(TimeStampMixin):

    company = models.ForeignKey(
        "company.Company",on_delete=models.CASCADE,null=True,
        related_name = "company_device"
    )
    device_name = models.CharField(
        max_length=200,null=True,
        verbose_name="Device Name"
    )
    # device type (laptop,mobile,tab etc)
    device_type = models.CharField(
        max_length=100,null=True,
        verbose_name="Device Type"
    )
    

    def __str__(self):
        return str(self.device_name)
    
    class Meta:
        verbose_name_plural = "Company Assets"


## Company Assets Deligate to Employee

class DeligateAssetstoEmployee(TimeStampMixin):

    asset = models.ForeignKey(
        "company.CompanyAssets",on_delete=models.CASCADE,null=True,
        related_name = "assigned_assets"
    )
    employee = models.ForeignKey(
        "accounts.Employee",on_delete=models.CASCADE,null=True,
        related_name = "assigned_employee"
    )

    ## information on Checking Out assets 
    checking_out_date = models.DateTimeField(
        auto_created=False,auto_now_add=False,null=True,
        verbose_name="Checking Out Date"
    )
    checking_out_condition_log = models.CharField(
        max_length=500,null=True,blank=True,
        verbose_name="Checking Out Condition"
    )

    ## information on Returning Assets 
    return_date = models.DateTimeField(
        auto_created=False,auto_now_add=False,null=True,
        verbose_name="Return Date"
    )
    return_condition_log = models.CharField(
        max_length=500,null=True,blank=True,
        verbose_name="Return Condition"
    )

    
    def __str__(self):
        return f"{self.asset} | {self.employee}"

    class Meta:
        verbose_name_plural = "Deligate Assets to Employees"