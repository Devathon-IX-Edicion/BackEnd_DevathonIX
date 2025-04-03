from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Recipe, RecipeIngredient
from .serializers import RecipeSerializer, RecipeIngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filterset_fields = ['difficulty', 'is_community_created', 'effect']
    search_fields = ['name', 'description']

    def create(self, request, *args, **kwargs):
        ingredients_data = request.data.pop('ingredients', [])
        serializer = self.get_serializer(
            data=request.data, 
            context={'ingredients': ingredients_data}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=True, methods=['get'])
    def ingredients(self, request, pk=None):
        recipe = self.get_object()
        ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        serializer = RecipeIngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

class RecipeIngredientViewSet(viewsets.ModelViewSet):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
    filterset_fields = ['recipe', 'ingredient']