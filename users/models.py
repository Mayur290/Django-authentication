from django.contrib.auth.models import AbstractUser
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list