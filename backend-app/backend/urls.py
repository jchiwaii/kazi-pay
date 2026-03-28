from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Optional: Documentation setup (Swagger) so you can test your APIs easily
schema_view = get_schema_view(
   openapi.Info(
      title="Kazipesa API",
      default_version='v1',
      description="Gig Platform with Escrow and M-Pesa Integration",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls), 

    # App-specific API Endpoints
   path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/client/', include('clients.urls')),
    path('api/worker/', include('workers.urls')),
    path('api/escrow/', include('escrow.urls')),
    path('api/wallet/', include('wallet.urls')),
    path('api/notifications/', include('notification.urls')),
    path('api/platform-admin/', include('adminApp.urls')), # Our custom admin logic

    # API Documentation (Swagger/ReDoc)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]