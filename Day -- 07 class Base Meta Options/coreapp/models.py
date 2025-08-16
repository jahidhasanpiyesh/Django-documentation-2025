from django.db import models


# Create your 1st models here.
class coreapp1(models.Model):
    note = models.CharField(max_length=500) #Field type for storing text with a max length.


# Create your 2nd models here.
class coreapp(models.Model):
    nm = models.CharField(max_length=100)

    class Meta:                             #Extra configuration: default ordering & how names appear in admin.
        ordering = ["nm"]                   #Sets default sorting order when fetching objects.
        # How the plural form of this model will be displayed in the admin site.
        verbose_name_plural = "Name"

# Create your 3rd models here.
class coreapp2(models.Model):
    tech = models.CharField(max_length=50)

    class Meta:
        ordering = ["tech"]
        #How the singular name of this model will be shown in the admin site.
        verbose_name = "technology"