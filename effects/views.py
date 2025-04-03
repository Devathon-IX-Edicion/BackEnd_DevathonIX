from rest_framework import viewsets
from .models import Effect
from .serializer import EffectSerializer

class EffectViewSet(viewsets.ModelViewSet):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer
    filterset_fields = ['type', 'rarity']
    search_fields = ['name', 'description']