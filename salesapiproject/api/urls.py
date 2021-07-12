from salesapiproject.api.views import ProductViewSet, ProductLotViewSet, ClientViewSet, OrderViewSet, OrderLineViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('productlots', ProductLotViewSet)
router.register('clients', ClientViewSet)
router.register('orders', OrderViewSet)
router.register('orderlines', OrderLineViewSet)
urlpatterns = router.urls
