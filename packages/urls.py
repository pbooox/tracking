"""Packages urls."""

# Django
from django.urls import path, include

# Django rest framework
from rest_framework.routers import DefaultRouter

# Views
import packages.views as packages_views

router = DefaultRouter()
router.register(r'packages', packages_views.PackageViewSet, basename='packages')


urlpatterns = [
    path('', include(router.urls))
]