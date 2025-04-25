from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Q
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
    
    @action(detail=False, methods=['post'])
    def find_by_ingredients(self, request):
        ingredient_ids = request.data.get('ingredients', [])
        
        if not ingredient_ids:
            return Response(
                {"error": "Please provide ingredient IDs"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Método 1: Usando el nuevo campo ingredient_ids
        recipes = Recipe.objects.filter(ingredient_ids__contains=ingredient_ids)
        
        # Método 2: Usando consultas más complejas (alternativa si no usas ArrayField)
        # Encuentra recetas que contienen TODOS los ingredientes especificados
        recipes_alt = Recipe.objects.filter(
            recipe_ingredients__ingredient_id__in=ingredient_ids
        ).annotate(
            matching_count=Count('recipe_ingredients', 
                             filter=Q(recipe_ingredients__ingredient_id__in=ingredient_ids))
        ).filter(
            matching_count=len(ingredient_ids)
        ).distinct()
        
        # Usa la consulta más adecuada según tu implementación
        serializer = self.get_serializer(recipes, many=True)
        return Response(serializer.data)

class RecipeIngredientViewSet(viewsets.ModelViewSet):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
    filterset_fields = ['recipe', 'ingredient']