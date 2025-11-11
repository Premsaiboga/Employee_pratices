from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(blank=False, null=False)
    Phone = models.IntegerField(max_length=12, blank=False,null=False)
    

    