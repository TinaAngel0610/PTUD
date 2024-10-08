from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank = False)
    
    def __str__(self):
        return self.title