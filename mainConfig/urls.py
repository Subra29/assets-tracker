
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from structure.accounts import views


## DRF ysgh settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Assets Tracker",
      default_version='v1',
      description="Assets Tracker Backend API",
      contact=openapi.Contact(email="contact@test.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    ## apps  url config 
    path('',include('structure.accounts.urls')),
    path('company/',include('structure.company.urls')),

    ## API authentication ENDPOINT
    path('api/token/', views.APILoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Redoc Documention
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

## static config 
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)