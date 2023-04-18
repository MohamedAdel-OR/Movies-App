from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Spoiler(models.Model):
    User=models.OneToOneField(User, on_delete= models.CASCADE)
    adress = models.CharField(max_length=60)
    adress2=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=60)
    zip_num=models.CharField(max_length=6)
    def __str__(self) :
        return self.User.username




