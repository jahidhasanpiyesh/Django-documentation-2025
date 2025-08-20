from django.db import models

# Create your models here.
class person(models.Model):
    first_name = models.CharField(max_length=50) # this field ar max langth 50 latter,,
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField() # use to date time bult in key word..

    def baby_status(self):
        import datetime

        if self.birth_date < datetime.date(2025, 2, 4):
            return "Pre-boomer"
        
        elif self.birth_date < datetime.date(2025, 2, 2):
            return "Baby-boomer"
        
        else:
            return "Post-boomer"
        
    @property
    def full_name(self):
        # "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"