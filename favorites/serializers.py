from rest_framework import serializers
from .models import FavoriteRecipe
from recipes.serializers import RecipeSerializer

class FavoriteRecipeSerializer(serializers.ModelSerializer):
    recipe_details = RecipeSerializer(source='recipe', read_only=True)
    
    class Meta:
        model = FavoriteRecipe
        fields = ['id', 'session_id', 'recipe', 'recipe_details', 'created_at']