from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    username = None
    email = models.EmailField('email', unique=True)
    first_name = models.CharField('first name', max_length=100, blank=True)
    last_name = models.CharField('last name', max_length=100, blank=True, null=False)