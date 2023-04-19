from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    note = models.TextField(blank=True, max_length=275)

    def __str__(self):
     return self.name

    def get_absolute_url(self):
     return reverse("detail", kwargs={"child_id": self.id})




class Roster(models.Model):
    date = models.DateField("Date Added")
    age_group = models.CharField(max_length=100)
    time_entered = models.TimeField(default='') 
    caregiver = models.CharField(max_length=100)
    dropped_off_by = models.CharField(max_length=100)
    enrolled_status = models.BooleanField(default=True)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.checkin_status} ({self.id})"
