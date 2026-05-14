from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredient = models.CharField(max_length=50)
    instruction = models.TextField()
    time = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}.recipe'
    
# model -> makemigrations -> migration file created -> migrate -> database reflect
# table_name: app_modelname