from rest_framework import serializers
from .models import Recipe, RecipeIngredient
from effects.serializer import EffectSerializer
from ingredients.serializer import IngredientSerializer

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_details = IngredientSerializer(source='ingredient', read_only=True)
    
    class Meta:
        model = RecipeIngredient
        fields = ['id', 'ingredient', 'ingredient_details', 'quantity', 'unit']

class RecipeSerializer(serializers.ModelSerializer):
    effect_details = EffectSerializer(source='effect', read_only=True)
    ingredients = RecipeIngredientSerializer(source='recipe_ingredients', many=True, read_only=True)
    
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'effect', 'effect_details', 
                  'difficulty', 'is_community_created', 'created_at', 'ingredients']
    
    def create(self, validated_data):
        ingredients_data = self.context.get('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        
        for ingredient_data in ingredients_data:
            RecipeIngredient.objects.create(recipe=recipe, **ingredient_data)
        
        return recipe
