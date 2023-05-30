from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    auteur = models.CharField(max_length=100)
    image = models.ImageField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)