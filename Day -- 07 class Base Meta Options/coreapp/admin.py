from django.contrib import admin
# Import your models from models.py
# Here you have three models: coreapp1, coreapp, and coreapp2
from .models import coreapp1, coreapp, coreapp2

# --------- Model registration section ---------
# Register your models here.
# admin.site.register() tells Django:
# "Show this model in the admin panel so it can be managed there."
# Register the coreapp1, coreapp, coreapp2 model with the admin site
admin.site.register(coreapp1)
admin.site.register(coreapp)
admin.site.register(coreapp2)
