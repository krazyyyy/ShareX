from django.db import models
from django.contrib.auth.models import AbstractUser
from django_cryptography.fields import encrypt
import random
import string
import os

def get_random_string():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(20))
    return result_str
    # print("Random string of length", length, "is:", result_str)

# Create your models here.
class User(AbstractUser):
    pass
    

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user")
    upload = models.FileField(upload_to="Files")
    uploaded_at = models.DateField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=128, default=get_random_string)
    encryption = models.BooleanField(default=False)

    def name_(self):
        t = f"{self.upload}"
        splitname = t.rsplit('/')
        return splitname[-1]

    
    # File().name_()
