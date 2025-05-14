from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    phone=models.CharField(max_length=10)
    message=models.TextField(max_length=200)

class Test(models.Model):
    email=models.EmailField(max_length=100, primary_key=True)
    fullname=models.CharField(max_length=120)
    phone=models.CharField(max_length=10)
    message=models.TextField(max_length=200)

    