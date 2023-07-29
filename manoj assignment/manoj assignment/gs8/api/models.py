from django.db import models
"This is the testing for new branch "
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)