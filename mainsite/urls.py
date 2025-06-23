from django.contrib import admin
from django.urls import include, path
from mainsite.views import Login, Logout, Register
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Octo Quiz API",
        default_version='v1',
        description="Documentação da API do Octo Quiz App",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="seuemail@exemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='home'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('quiz/', include('quiz.urls')),
    
    path('api/', include('quiz.api_urls')),
    path('api/auth/', obtain_auth_token, name='api_token_auth'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
