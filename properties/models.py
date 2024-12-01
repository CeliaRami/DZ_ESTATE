from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50, choices=[('house', 'House'), ('apartment', 'Apartment')])
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    contact_info = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='property_photos/', blank=True, null=True)  # New field for photos
    
    def __str__(self):
        return self.title
