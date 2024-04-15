from django.db import models

class Feature(models.Model):
    # id:int not required as models.Model is inherited.
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)
    
