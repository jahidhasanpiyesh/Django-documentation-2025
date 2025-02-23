from django.db import models

# Create your models TEST 1
# class person(models.Model):
#     name = models.CharField(max_length=70)

#     # Using to drop down 2 simple example.
#     SHART_SIZE = {
#         "S": "Small",
#         "M": "Medium",
#         "L": "Large",
#     }

#     color = {
#         "B": "Black",
#         "R": "Red",
#         "W": "White",
#     }

#     # Using to choices key-word and show admin site this fields to connect to drop down.
#     shart_size = models.CharField(max_length=1, choices=SHART_SIZE)
#     shart_color = models.CharField(max_length=1, choices=color)


# Create your models TEST 2
# class Runner(models.Model):
#     name = models.CharField(max_length=60)
#     MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
#     medal = models.CharField(blank=True, choices=MedalType, max_length=10)


# Create your models TEST 3 two way 
# class fFruit(models.Model):
#     # Show of Primary key of indexing.
#     F_name = models.CharField(max_length=100, primary_key=False)

# class sFruit(models.Model):
#     # Not Show of Primary key of indexing // show of char name of fields.
#     S_name = models.CharField(max_length=100, primary_key=True)
    


# Create your models TEST 4
class troll(models.Model):
    id = models.BigAutoField(primary_key=True)


# Test is wrong this code is not working.
# class froll(models.Model):
#     id = models.BigAutoField(primary_key=False)