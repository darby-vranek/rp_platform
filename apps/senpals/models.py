from django.db import models
from django.contrib.auth.models import AbstractUser


# user
class User(AbstractUser):
    def by_user(self):
        return f"by {self.username}"


# abstracts
class Model(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
