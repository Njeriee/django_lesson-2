from django.db import models

# Create your models here.
class Authors(models.Model):
    first_name = models.CharField(max_length= 30)
    middle_name = models.CharField(max_length= 30)
    sur_name = models.CharField(max_length= 30)

class Books(models.Model):
    title = models.CharField(max_length= 30)
    author = models.ManyToManyField(Authors)
    publisher = models.CharField(max_length= 30)
    price = models.IntegerField()