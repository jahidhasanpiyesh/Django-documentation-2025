from django.contrib import admin
from .models import home
from .first_models import first
from .secend_models import second
# Register your models here.

admin.site.register(home)
admin.site.register(first)
admin.site.register(second)