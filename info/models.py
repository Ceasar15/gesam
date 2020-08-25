from django.db import models

# Create your models here.


class People(models.Model):
    fullname = models.CharField(max_length=50, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    hall = models.CharField(max_length=50, null=False, blank=False)
    roomNumber = models.CharField(max_length=15, blank=True)
    program = models.CharField(max_length=50, null=False, blank=False)
    birthday = models.DateField(blank=False)
    gender = models.CharField(null=True, max_length=15)
    level = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(People)
