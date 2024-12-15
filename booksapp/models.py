from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    file = models.FileField(upload_to='books/', null=True)
    image = models.ImageField(upload_to='images/', null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title