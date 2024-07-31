from django.db import models
from django.contrib.auth.models import User

# Model for customers
class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    name = models.CharField(max_length=100)
    address = models.TextField()
    user = models.OneToOneField(User, related_name='customer_profile',  on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    delete_status=models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name