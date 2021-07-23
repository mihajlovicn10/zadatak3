from django.db import models

# Create your models here.


class Book(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField (max_length=500)

class Api(models.Model): 
    user = models.CharField(max_length=100)
    mode = models.BooleanField()
    value = models.CharField(max_length=100)
    

    