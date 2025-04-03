from django.db import models

# Modelo de prueba
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name