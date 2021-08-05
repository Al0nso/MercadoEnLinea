from django.db import models

from applications.person.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250)
    price = models.FloatField(blank=False, default=1.0)
    is_sold = models.BooleanField(default=False, blank=False)
    photo = models.ImageField(upload_to='product', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
