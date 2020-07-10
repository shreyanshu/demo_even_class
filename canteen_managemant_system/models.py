from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CookInfo(models.Model):
    phone_no = models.CharField(max_length=12)
    pan_no = models.IntegerField()


class Cook(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    info = models.OneToOneField(CookInfo, on_delete=models.PROTECT, null=True)
    profile_pic = models.ImageField(upload_to='cook', null=True)

    def __str__(self):
        return self.name #+ ' ' + str(self.age)


class Speciality(models.Model):
    name = models.CharField(max_length=15)
    cook = models.ManyToManyField(Cook)


class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    qty = models.IntegerField()
    price = models.IntegerField()
    discount = models.FloatField(default=0)
    cook = models.ForeignKey(Cook, on_delete=models.PROTECT, null=True)




