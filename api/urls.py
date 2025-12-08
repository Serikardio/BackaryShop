from rest_framework import routers
from .views import ClientViewSet, PasswordViewSet, OrderViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'passwords', PasswordViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = router.urls
