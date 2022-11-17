from rest_framework import routers

from .api.viewsets import TransactionViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls
