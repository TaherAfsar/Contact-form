import email
from django.db import models
from django.forms import CharField, DateField, IntegerField

# Create your models here.
class Contact(models.Model):
    serial = 3
    serial = models.IntegerField()
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self) :
        return self.name


