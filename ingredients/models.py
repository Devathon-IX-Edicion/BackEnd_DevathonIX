from django.db import models

# Modelo de prueba
class Ingredient(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name