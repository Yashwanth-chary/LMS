"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('library.urls')),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# Import your existing routers and viewsets
from library.urls import router as library_router
from django.contrib.auth import views as auth_views

# Schema view for Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Library Management API",
        default_version='v1',
        description="API documentation for Library Management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# A permissions.IsAuthenticated,

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('library.urls')),  # Include the app's URLs
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("library.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # JWT Authentication URLs
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]