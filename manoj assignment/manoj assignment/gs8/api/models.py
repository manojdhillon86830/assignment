from django.db import models
"This is the testing for dhillon sirK "
'''Hello Friends'''
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)