from django.db import models

# Create your models here.

class address(models.Model):
    name=models.CharField(max_length=250)
    ad_l1=models.CharField(max_length=250,blank=True)
    ad_l2=models.CharField(max_length=250,blank=True)
    lat=models.DecimalField(max_digits=120,decimal_places=11)
    long = models.DecimalField(max_digits=120, decimal_places=11)



