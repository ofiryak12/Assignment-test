

# class Product(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField(blank=True,null=True)
#     price = models.DecimalField(decimal_places=2,max_digits=1000)
#     summary = models.TextField(default='This is awesome!',null=False)
#     featured = models.BooleanField(null=True)

from django.db import models
from django.conf import settings

class Token(models.Model):
    ...

    class Meta:
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS

class Data_msg(models.Model):
    sender          = models.CharField(max_length=100)
    reciever        = models.CharField(max_length=100)
    message         = models.TextField()
    subject         = models.CharField(max_length=50)
    read            = models.BooleanField(default=False)
    creation_Date   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender
# Create your models here.
