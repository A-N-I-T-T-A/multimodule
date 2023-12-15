from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
class CustomUser(AbstractUser):
    user_type=models.CharField(default=1, max_length=10)

class Usermember(models.Model):

    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    age=models.IntegerField()
    phone=models.CharField(max_length=255)
    Image=models.ImageField(blank=True,upload_to="image/",null=True)
