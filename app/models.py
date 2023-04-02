from django.db import models
import uuid as uuid_lib

class Position(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

# Create your models here.
class Employee(models.Model):
    id = models.UUIDField(
        default=uuid_lib.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    salary = models.IntegerField(default = 0)
    position = models.ForeignKey(Position,on_delete = models.CASCADE)
    mobile = models.CharField(max_length = 10)