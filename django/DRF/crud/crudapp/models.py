from django.db import models

# Create your models here.
class employeee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=32)
    esal=models.IntegerField()
