from salesapiproject.api.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)
urlpatterns = router.urls
