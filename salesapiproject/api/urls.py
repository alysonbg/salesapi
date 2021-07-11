from salesapiproject.api.views import ProductViewSet, ProductLotViewSet, ClientViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('productlots', ProductLotViewSet)
router.register('clients', ClientViewSet)
router.register('orders', OrderViewSet)
urlpatterns = router.urls
