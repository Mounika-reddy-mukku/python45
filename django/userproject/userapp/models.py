from django.db import models

# Create your models here.
class user(models.Model):
    uid=models.IntegerField()
    uname=models.CharField(max_length=32)
