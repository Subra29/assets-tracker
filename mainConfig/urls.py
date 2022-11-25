
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from structure.accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    ## apps  url config 
    path('',include('structure.accounts.urls')),
    path('company/',include('structure.company.urls')),

    ## API authentication ENDPOINT
    path('api/token/', views.APILoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

## static config 
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)