from django.db import models
from datetime import datetime

class Realtor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    is_MVP = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name