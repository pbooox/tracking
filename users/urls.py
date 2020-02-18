"""User urls."""

# Django
from django.urls import path, include

# Django rest framework
from rest_framework.routers import DefaultRouter

# Views
import users.views as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls))
]