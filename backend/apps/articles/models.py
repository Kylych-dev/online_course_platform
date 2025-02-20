from django.db import models

from django.contrib.auth.models import PermissionsMixin
from apps.users.models import CustomUser


class Article(models.Model):

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
