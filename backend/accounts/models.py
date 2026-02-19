from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models
# https://django-phonenumber-field.readthedocs.io/en/latest/


class NewUser(AbstractUser):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    avatar = models.ImageField(default='uploads/default4', upload_to='uploads/accounts_pictures/', blank=True)
    username = None
    USERNAME_FIELD = 'phone'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'email']
