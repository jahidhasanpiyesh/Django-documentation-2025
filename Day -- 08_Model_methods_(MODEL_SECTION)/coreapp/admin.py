from django.contrib import admin
from .models import person
# Register your models here.
# Show model file..
@admin.register(person)
class personaladmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'full_name', 'birth_date', 'baby_status')
    search_fields = ('first_name', 'last_name')
    list_filter = ('birth_date',)
