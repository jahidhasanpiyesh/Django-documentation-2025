from django.db import models

# Create a 2 class base models type of 4 fields
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class school(models.Model):
    name = models.CharField(max_length=100)
    data = models.DateField()
    room = models.IntegerField()
    #creates a foreign key relationship between the Musician model and the model in which this line is used.
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)