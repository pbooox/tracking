"""Shipment views."""

# Django rest framework
from rest_framework import viewsets, mixins
from rest_framework.views import APIView 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from Shipments.permissions import IsClientShipp
# Serializers
from Shipments.serializer import ShipmentModelSerializer, Shipment_detailModelSerializer, ShipmentdetailSerializer
from packages.serializers import PackageModelSerializer


# from cride.circles.serializers import CircleModelSerializer

# Models
from Shipments.models import Shipment, Shipment_detail
from users.models import User
from packages.models import Package
# from cride.circles.models import Circle, Membership


class ShipmentViewSet(viewsets.ModelViewSet):
    """Circle view set."""

    
    
    serializer_class = ShipmentModelSerializer
    queryset = Shipment.objects.all()


    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action in ['create', 'list', 'update', 'partial_update']:
            permissions.append(IsAdmin)
        if self.action in ['retrieve']:
            permissions.append(IsClientShipp)
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.request.data['user'])
        shipment = serializer.save(user=user)

    @action(detail=False, methods=['get'])
    def report(self, request):
        warehouse = Shipment.objects.filter(state=1).count()
        going = Shipment.objects.filter(state=2).count()
        delivered = Shipment.objects.filter(state=3).count()
        data = {
            'total': Shipment.objects.all().count(),
            'warehouse': warehouse,
            'going': going,
            'delivered': delivered
        }
        return Response(data, status=status.HTTP_200_OK)



class Shipment_detailAPIView(APIView):
    """"""
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = ShipmentdetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        detail = serializer.save()
        data = {
            'detail': ShipmentdetailSerializer(detail).data
        }
        return Response(data, status=status.HTTP_201_CREATED)
