from django.db import models
from django.contrib.auth.models import User


class Messages(models.Model):
    UserName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=50)
    Message = models.TextField(max_length=300)

    def __str__(self):
        return self.UserName


class City(models.Model):

    Cid = models.IntegerField(primary_key=True)
    CityName = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Special_Offer = models.BooleanField(default=False)
    Citypic = models.ImageField(upload_to='pics', null=True)
    Depart_date = models.CharField(max_length=100,default="")


    def __str__(self):
        return self.CityName


class Order(models.Model):
    UserName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    CityName = models.CharField(max_length=100)
    Total = models.CharField(max_length=100)
    Booking_date = models.CharField(max_length=100,default="")
    Depart_date = models.CharField(max_length=100,default="")
    
    def __str__(self):
        return self.UserName
