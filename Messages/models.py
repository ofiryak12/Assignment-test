from django.db import models
from django.conf import settings

# In this file we will be creating the model for our Database

class Token(models.Model):
    ...

    class Meta:
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS

# Data_msg is the model i am going to work with,
# in includes all of the fields which were required to create a message,
# like a boolean field for read or not and creation date
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
