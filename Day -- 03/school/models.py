from django.db import models

# Create your Verbose field names models

class normal(models.Model):
    # Normal fields verbose not useing.
    first_name = models.CharField(max_length=30)

class Verbose(models.Model):
    # verbose use fields.
    first_name = models.CharField("person's first name", max_length=30)