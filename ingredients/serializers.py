from rest_framework import serializers
from ingredients.models import Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    date_created = serializers.DateTimeField(format="%d/%m/%Y")

    class Meta:
        model = Ingredient
        fields = '__all__', 'cateogry'
	
