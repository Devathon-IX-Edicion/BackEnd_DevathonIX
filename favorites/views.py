from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import FavoriteRecipe
from .serializers import FavoriteRecipeSerializer

class FavoriteRecipeViewSet(viewsets.ModelViewSet):
    queryset = FavoriteRecipe.objects.all()
    serializer_class = FavoriteRecipeSerializer
    filterset_fields = ['session_id', 'recipe']
    
    def get_queryset(self):
        queryset = FavoriteRecipe.objects.all()
        session_id = self.request.query_params.get('session_id', None)
        if session_id is not None:
            queryset = queryset.filter(session_id=session_id)
        return queryset
    
    @action(detail=False, methods=['get'])
    def by_session(self, request):
        session_id = request.query_params.get('session_id', None)
        if session_id is None:
            return Response({"error": "session_id parameter is required"}, status=400)
        
        favorites = FavoriteRecipe.objects.filter(session_id=session_id)
        serializer = self.get_serializer(favorites, many=True)
        return Response(serializer.data)