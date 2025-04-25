from django.db import models
from django.contrib.postgres.fields import ArrayField
from effects.models import Effect
from ingredients.models import Ingredient

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    effect = models.ForeignKey(Effect, on_delete=models.CASCADE, related_name='recipes')
    difficulty = models.IntegerField()  # nivel de dificultad (1-5)
    is_community_created = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Nuevo campo para almacenar IDs de ingredientes
    ingredient_ids = ArrayField(models.IntegerField(), blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Actualizar ingredient_ids basado en las relaciones existentes
        if self.pk:  # Si la receta ya existe
            self.ingredient_ids = list(self.recipe_ingredients.values_list('ingredient_id', flat=True))
        super().save(*args, **kwargs)
        
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_recipes')
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ingredient.name} for {self.recipe.name}"