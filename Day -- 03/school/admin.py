from django.contrib import admin
from .models import Verbose, normal
# Register your models here.

admin.site.register(normal)
admin.site.register(Verbose)
