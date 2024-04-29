from rest_framework import serializers
from .models import Vendor, PurchaseOrder, VendorPerformance


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'contact_details', 'address', 'vendor_code']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor_name = serializers.SerializerMethodField()

    def get_vendor_name(self, obj):
        return obj.vendor.name if obj.vendor else None

    class Meta:
        model = PurchaseOrder
        fields = ['po_number', 'vendor_name', 'order_date',
                  'delivery_date', 'items', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date']

    def to_representation(self, instance):
        # Prefetch the related vendor
        instance = PurchaseOrder.objects.select_related('vendor').get(pk=instance.pk)
        return super().to_representation(instance)


class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'on_time_delivery_rate', 'quality_rating_avg',
                  'average_response_time', 'fulfillment_rate']


class AcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['acknowledgment_date']