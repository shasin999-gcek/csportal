from django.db import models

class Students(models.Model) :
    rollNum = models.IntegerField()
    name =  models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    sem = models.CharField(max_length=2)


