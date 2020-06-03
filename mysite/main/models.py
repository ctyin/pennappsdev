from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
