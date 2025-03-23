from django.contrib import admin
from .models import user, Song
# Register your models here.

#-----------------------------Many-to-one relationships--------------------- ?
# from .models import user, post

# @admin.register(user)
# class register(admin.ModelAdmin):
#     list_display = ["name","password"]

# admin.site.register(post)


# ------------------------Many to Many Relationship-------------------------?
# @admin.register(user)
# class register(admin.ModelAdmin):
#     list_display = ["name","password"]

# admin.site.register(Song)


# ------------------- One to One Relationship------------------------------?
admin.site.register(user)
admin.site.register(Song)