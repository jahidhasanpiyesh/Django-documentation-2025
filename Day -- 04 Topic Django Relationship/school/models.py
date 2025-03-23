from django.db import models

# -----------------------------Many-to-one relationships--------------------- ?
# class user(models.Model):
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)

# class post(models.Model):
#     user = models.ForeignKey(user, on_delete=models.CASCADE)
#     post_title = models.CharField(max_length=300)
#     post_cat = models.CharField(max_length=200)
#     post_publish_date = models.DateTimeField()

# ------------------------Many to Many Relationship-------------------------?
# class user(models.Model):
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)

# class Song(models.Model):
#     user = models.ManyToManyField(user)
#     song_name = models.CharField(max_length=100)
#     song_durations = models.IntegerField()


# ------------------------One to One Relationship-------------------------?
class user(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Song(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    song_durations = models.IntegerField()