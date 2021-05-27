from django.db import models

# Create your models here.
class ToDo(models.Model):        
    userId= models.IntegerField
    id = models.IntegerField
    title = models.CharField
    completed=models.BooleanField

    def __str__(self) :
        return (self.title)
    