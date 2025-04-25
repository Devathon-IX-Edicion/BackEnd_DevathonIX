from rest_framework import serializers
from .models import Recipe, RecipeIngredient
from effects.serializer import EffectSerializer
from ingredients.serializers import IngredientSerializer

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_details = IngredientSerializer(source='ingredient', read_only=True)
    
    class Meta:
        model = RecipeIngredient
        fields = ['id', 'ingredient', 'ingredient_details', 'quantity', 'unit']

class RecipeSerializer(serializers.ModelSerializer):
    effect_details = EffectSerializer(source='effect', read_only=True)
    ingredients = RecipeIngredientSerializer(source='recipe_ingredients', many=True, read_only=True)
    ingredient_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'effect', 'effect_details', 
                  'difficulty', 'is_community_created', 'created_at', 
                  'ingredients', 'ingredient_ids']
    
    def create(self, validated_data):
        ingredients_data = self.context.get('ingredients', [])
        ingredient_ids = validated_data.pop('ingredient_ids', [])
        recipe = Recipe.objects.create(**validated_data)
        
        # Crear RecipeIngredient desde los datos proporcionados
        for ingredient_data in ingredients_data:
            RecipeIngredient.objects.create(recipe=recipe, **ingredient_data)
        
        # Actualizar ingredient_ids
        recipe.ingredient_ids = list(recipe.recipe_ingredients.values_list('ingredient_id', flat=True))
        recipe.save(update_fields=['ingredient_ids'])
        
        return recipe