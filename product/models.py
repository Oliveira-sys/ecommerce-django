from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    img = models.ImageField(upload_to='products/', blank=True, null=True)
