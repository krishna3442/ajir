from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    clas=models.CharField(max_length=20)
    marks=models.IntegerField(max_length=10)



    def __str__(self):
        return self.name
