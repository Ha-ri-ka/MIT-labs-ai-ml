from django.db import models

# Create your models here.
class works(models.Model):
    person_name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    salary=models.IntegerField()

class lives(models.Model):
    person_name=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
