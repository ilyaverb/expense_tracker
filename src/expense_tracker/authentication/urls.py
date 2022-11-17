from django.urls import path

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from expense_tracker.authentication.api.viewsets import UserViewSet
from expense_tracker.authentication.api.views import ProfileView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path(route='profiles/<uuid:user__uid>/', view=ProfileView.as_view(), name='profiles'),
    path(route='token/', view=obtain_auth_token, name='auth_token')
]

urlpatterns += router.urls
