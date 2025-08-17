from django.db import models

# Create your models here.
class person(models.Model):
    first_name = models.CharField(max_length=50) # this field ar max langth 50 latter,,
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField() # use to date time bult in key word..

    def baby_status(self):
        import datetime

        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"