from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, max_length=19,)
    completed = models.BooleanField(default=False)
    if completed ==True: 
        completed_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_date',)
        
    def __str__(self):
        return self.content