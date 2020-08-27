# Create your models here.
from django.db import models

# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(null=True, max_length=100, blank=True)
    email = models.EmailField(default="kwadwo123@gmail.com", max_length=100, blank=True)
    phone = models.IntegerField(null=True, blank=False)
    message = models.TextField(max_length=300, blank=False)

    def __str__(self):
        return str(self.fullname)


class People(models.Model):
    fullname = models.CharField(max_length=100, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    hall = models.CharField(max_length=100, null=False, blank=False)
    roomNumber = models.CharField(max_length=100, blank=True)
    program = models.CharField(max_length=50, null=False, blank=False)
    birthday = models.DateField(max_length=100,blank=False)
    gender = models.CharField(null=True, max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return str(People)
