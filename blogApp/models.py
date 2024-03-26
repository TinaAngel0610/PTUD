from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    user_name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(blank = False)
    updated_at = models.DateTimeField(blank = False)
    
    def __str__(self):
        return self.title
