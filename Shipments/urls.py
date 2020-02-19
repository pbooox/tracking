"""Packages urls."""

# Django
from django.urls import path, include

# Django rest framework
from rest_framework.routers import DefaultRouter

# Views
import Shipments.views as shipments_views
from Shipments.views import Shipment_detailAPIView

# router2 = DefaultRouter()
# router2.register(r'detail', shipments_views.Shipment_detail, basename='detail')

router = DefaultRouter()
router.register(r'shipments', shipments_views.ShipmentViewSet, basename='shipments')



urlpatterns = [
    path('', include(router.urls)),
    path('detail/', Shipment_detailAPIView.as_view(), name='detail'),

]