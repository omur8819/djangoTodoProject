from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ('-created_date',)
        
    def __str__(self):
        return self.content
    
    def save(self, *args, **kwargs):
        if self.completed:
            self.completed_date = timezone.now()
        return super().save(*args, **kwargs)