from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default = uuid.uuid4, editable = False, primary_key = True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        abstract = True
        
class detail(BaseModel):
    type = models.CharField(max_length = 70)
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    profile_pic = models.ImageField(upload_to = 'images')
    username  = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 50)

    def __str__(self):
       return self.fname 


