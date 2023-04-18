from django.db import models

# Create your models here.
class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    note = models.TextField(max_length=275)

def __str__(self):
    return self.name
