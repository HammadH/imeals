from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib import admin


class User(AbstractUser):
	mobile = models.CharField(max_length=10, blank=False)
	address = models.TextField(blank=False)





admin.site.register(User)