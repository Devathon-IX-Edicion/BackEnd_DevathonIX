from rest_framework import serializers
from .models import Ingredient
## Ojo serializador de prueba
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


