from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True) # deletes the child task of the user if they get deleted, null true means could be empty field, blank for the form could also be true
    title = models.CharField(max_length=200) # describes max length
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False) # when a task is created it should not be done
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete'] #orders a query set so that complete items are sent to the bottom