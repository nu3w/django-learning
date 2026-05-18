from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredient = models.CharField(max_length=50)
    instruction = models.TextField()
    time = models.IntegerField()
    level = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
# model -> makemigrations -> migration file created -> migrate -> database reflect
# table_name: app_modelname