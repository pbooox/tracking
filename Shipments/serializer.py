"""Shipment serializer."""

# Django rest framework
from rest_framework import serializers

# serializers
from users.serializers import UserModelSerializer

# Model
from Shipments.models import Shipment, Shipment_detail
from packages.models import Package

class ShipmentModelSerializer(serializers.ModelSerializer):
    """Shipment model serializer."""

    

    class Meta:
        """Meta class."""

        model = Shipment
        fields=(
            'id',
            'user',
            'date',
            'price',
            'state',
            'location',
            'packages',
        )
        depth = 1


class Shipment_detailModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment_detail
        fields=(
            'shipment',
            'package'
        )



class ShipmentdetailSerializer(serializers.Serializer):
    shipment = serializers.CharField(max_length=1)
    package = serializers.CharField(max_length=1)

    def create(self,data):
        shipment1 = Shipment.objects.get(id=data['shipment'])
        package1 = Package.objects.get(id=data['package'])
        detail = Shipment_detail.objects.create(shipment=shipment1, package=package1)
        return detail  




class ShipmentReportsSerializer(serializers.Serializer):
    """"""
    
    




