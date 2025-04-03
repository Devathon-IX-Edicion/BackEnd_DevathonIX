from django.db import models
from recipes.models import Recipe

class FavoriteRecipe(models.Model):
    session_id = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session_id', 'recipe')

    def __str__(self):
        return f"Favorite: {self.recipe.name} (Session: {self.session_id})"