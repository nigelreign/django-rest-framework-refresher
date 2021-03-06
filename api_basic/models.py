from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, default="title")
    author = models.CharField(max_length=100, default="author")
    email = models.EmailField(max_length=100, default="email")
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
