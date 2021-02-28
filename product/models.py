from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length required
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    summary = models.TextField(default="Hello World")
    featured = models.BooleanField(default=True) # or, you can also say null=True