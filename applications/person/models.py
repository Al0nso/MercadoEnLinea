from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    BUYER = '0'
    SELLER = '1'
    TYPE_USER = [
        (BUYER, 'Comprador'), 
        (SELLER, 'Vendedor'),
    ]

    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    money = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    phone = models.CharField(max_length=10, blank=True)
    user_type = models.CharField(max_length=1, choices=TYPE_USER, blank=False, default=BUYER)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

