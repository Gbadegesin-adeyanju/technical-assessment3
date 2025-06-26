from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Author(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return f"{self.title} by {self.author.first_name} {self.author.last_name}"
