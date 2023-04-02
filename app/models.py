from django.db import models

class Position(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    salary = models.IntegerField(default = 0)
    position = models.ForeignKey(Position,on_delete = models.CASCADE)
    mobile = models.CharField(max_length = 100)