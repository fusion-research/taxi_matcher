from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    dest = models.CharField(max_length=30)
    time1 = models.IntegerField(max_length=4)
    time2 = models.IntegerField(max_length=4)
    course = models.CharField(max_length=30)
    liv_group = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.name

class Number(models.Model):
   num = models.IntegerField(max_length=4)
