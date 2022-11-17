from django.urls import path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Expense accounting manager API',
        default_version='v1',
        description='API',
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path(
        route='docs/',
        view=schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
