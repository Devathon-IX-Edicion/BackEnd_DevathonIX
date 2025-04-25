from rest_framework import serializers
from .models import Effect

class EffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effect
        fields = ['id', 'name', 'description', 'type', 'rarity', 'created_at']