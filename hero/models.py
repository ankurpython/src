from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=(('M','Male'),('F','Female')),default='F')
    movie = models.CharField(max_length=100)
