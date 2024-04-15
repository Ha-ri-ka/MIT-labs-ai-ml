from django.db import models
# A publisher table has a name, a street address, a city, 
# a state/ province, a country, and a Web site. A book table has a title and a 
# publication date. It also has one or more authors (a many-to-many relationship 
# with authors) and a single publisher (a one-to-many relationship - aka foreign 
# key - to publishers)
# Create your models here.
class author(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()

class publisher(models.Model):
    name=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)

class book(models.Model):
    title=models.CharField(max_length=50)
    date=models.DateField()