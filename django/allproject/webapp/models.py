from django.db import models

# Create your models here.
class registeruser(models.Model):
    uname=models.CharField(max_length=32)
    uemail=models.CharField(max_length=32)
    unum=models.IntegerField()
    upass=models.CharField(max_length=32)
    upass1=models.CharField(max_length=32)

