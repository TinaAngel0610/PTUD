from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    