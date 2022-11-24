from django.contrib import admin
from structure.company.models import (
    Company,
    EmployeeOfCompany,
    CompanyAssets,
    DeligateAssetstoEmployee
)


admin.site.register(Company)
admin.site.register(EmployeeOfCompany)
admin.site.register(CompanyAssets)
admin.site.register(DeligateAssetstoEmployee)
