from django.db import models
from django.db.models import JSONField
from django.core.exceptions import ValidationError


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    PURCHASE_STATUS = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    QUALITY_RATING_CHOICES = [
        (1.0, "1 - Poor"),
        (2.0, "2 - Below Average"),
        (3.0, "3 - Average"),
        (4.0, "4 - Good"),
        (5.0, "5 - Excellent"),
    ]
    po_number = models.CharField(max_length=255, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=PURCHASE_STATUS, default='pending')
    quality_rating = models.FloatField(choices=QUALITY_RATING_CHOICES, null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    # def clean(self):
    #     if self.delivery_date < self.order_date:
    #         raise ValidationError("Delivery date must be after order date.")
    #     else:
    #         # Handle the case when either order_date or delivery_date is None
    #         raise ValidationError("Both order date and delivery date must be set.")
    def __str__(self):
        return f"PO-{self.po_number} for {self.vendor.name}"


class VendorPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
