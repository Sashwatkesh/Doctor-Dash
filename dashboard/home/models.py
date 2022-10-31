from unicodedata import name
from django.db import models

# Create your models here.
class Contact_us(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 12)
    mess = models.TextField()

    
    def __str__(self) -> str:
        return 'Message from ' + self.name 

    