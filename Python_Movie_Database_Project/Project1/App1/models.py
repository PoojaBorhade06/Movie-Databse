from django.db import models

# Create your models here.
class MovieRecord(models.Model):
    Movie_Name=models.CharField(max_length=34)
    Release_date=models.DateField()
    Movie_starcast=models.CharField(max_length=34)
    Movie_Director=models.CharField(max_length=256)



