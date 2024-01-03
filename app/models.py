from django.db import models

# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sprinciple=models.CharField(max_length=100)
    Sbranch=models.CharField(max_length=100)
    def __str__(self):
        return self.Sname