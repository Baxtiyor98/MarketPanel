from shop.views import CategoryAPIView,ProductsAPIView,SaleAPIView,CardAPIView,CasherAPIView,VolumeAPIView
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register(r'category', CategoryAPIView, basename='category')
router.register(r'product', ProductsAPIView, basename='product')
router.register(r'sale', SaleAPIView, basename='sale')
router.register(r'casher', CasherAPIView, basename='casher')
router.register(r'volume', VolumeAPIView, basename='volume')
router.register(r'card', CardAPIView, basename='card')

urlpatterns = router.urls
#
# urlpatterns += [
#     path('books/', BookApiView.as_view(), name='books'),
#     path('books/<int:pk>/', RetrieveBookApiView.as_view(), name='retrieve-books'),
# ]