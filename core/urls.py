from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="User Calc API",
      default_version='v1',
      description="User Calc API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@usercal.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
