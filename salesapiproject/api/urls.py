from salesapiproject.api.views import ProductViewSet, ProductLotViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('productlots', ProductLotViewSet)
urlpatterns = router.urls
