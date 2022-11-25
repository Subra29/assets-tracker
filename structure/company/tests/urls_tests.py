'''
This file contains 
    - URL testing '
'''

from django.test import SimpleTestCase
from django.urls import (
    resolve,
)

from structure.company.views.company_view import (
    CompanyView,
    AssignEmployeetoComapnyView
)
from structure.company.views.assets_view import (
    CompanyAssetsView,
    AssignAssetstoEmployeeView,
    DeviceLogView,
)

## Company URL test
class CompanyTestURL(SimpleTestCase):

    def test_Company_URL (self):
        resolver = resolve('/')
        self.assertEqual(resolver.func.__name__,CompanyView.as_view().__name__)

    def test_AssignEmployee_URL (self):
        resolver = resolve('/company/add/employee/')
        self.assertEqual(resolver.func.__name__,AssignEmployeetoComapnyView.as_view().__name__)

## Assets URL test
class AssetTestURL(SimpleTestCase):

    def test_Asset_URL (self):
        resolver = resolve('/company/assets/')
        self.assertEqual(resolver.func.__name__,CompanyAssetsView.as_view().__name__)

    def test_AssignAssettoEmployee_URL (self):
        resolver = resolve('/company/assign/assets/')
        self.assertEqual(resolver.func.__name__,AssignAssetstoEmployeeView.as_view().__name__)

    def test_DeviceLog_URL (self):
        resolver = resolve('/company/assets/log/')
        self.assertEqual(resolver.func.__name__,DeviceLogView.as_view().__name__)