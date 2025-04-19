from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from category.models import Category
from category.serializers import CategorySerializer
from ingredients.models import Ingredient

class Class1(APIView):
    def get(self, request):
        categories = Category.objects.all().order_by('-id')
        serializer = CategorySerializer(categories, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get("name")
        if not name:
            return Response({"status": "error", "message": "The name field is required."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            category = Category.objects.create(name=name)
            return Response({"status": "ok", "message": "Category created successfully."},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Class2(APIView):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        return Response({"data": {
            "id": category.id,
            "name": category.name,
            "slug": category.slug
        }}, status=status.HTTP_200_OK)

    def put(self, request, id):
        name = request.data.get("name")
        if not name:
            return Response({"status": "error", "message": "The name field is required."},
                            status=status.HTTP_400_BAD_REQUEST)
        category = get_object_or_404(Category, pk=id)
        category.name = name
        category.slug = slugify(name)
        category.save()

        return Response({"status": "ok", "message": "Category updated successfully."},
                        status=status.HTTP_200_OK)

    def delete(self, request, id):
        category = get_object_or_404(Category, pk=id)

        if Ingredient.objects.filter(category_id=id).exists():
            return Response({"status": "error", "message": "Cannot delete category: linked ingredients exist."},
                            status=status.HTTP_400_BAD_REQUEST)

        category.delete()
        return Response({"status": "ok", "message": "Category deleted successfully."},
                        status=status.HTTP_200_OK)
