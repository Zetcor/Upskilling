from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
