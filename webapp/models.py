from django.db import models

# Create your models here.
class emp(models.Model):
    empid=models.IntegerField
    empname=models.CharField(max_length=100)
    emploc=models.CharField(max_length=100)

