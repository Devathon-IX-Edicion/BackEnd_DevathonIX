from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from .models import Ingredient, Category
from django.utils.dateformat import DateFormat

MAGIC_LEVEL_CHOICES = (
    ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"),
    ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10"),
)

class IngredientList(APIView):
    
    def get(self, request):
        ingredients = Ingredient.objects.order_by('-id').all()
        data = [{
            "id": ing.id,
            "name": ing.name,
            "slug": ing.slug,
            "description": ing.description,
            "magic_level": ing.magic_level,
            "preparation_time": ing.preparation_time,
            "category": ing.category.name,
            "date_created": DateFormat(ing.date_created).format('d/m/Y')
        } for ing in ingredients]
        return JsonResponse({"data": data}, safe=False)
    
    def post(self, request):
        required_fields = ['name', 'preparation_time', 'description', 'category_id', 'magic_level']
        for field in required_fields:
            if not request.data.get(field):
                return JsonResponse(
                    {"status": "error", "message": f"The {field} field is required"},
                    status=HTTPStatus.BAD_REQUEST
                )

        try:
            category = Category.objects.get(pk=request.data["category_id"])
        except Category.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Invalid category ID"},
                status=HTTPStatus.BAD_REQUEST
            )

        if request.data["magic_level"] not in [choice[0] for choice in MAGIC_LEVEL_CHOICES]:
            return JsonResponse(
                {"status": "error", "message": "Invalid magic level value"},
                status=HTTPStatus.BAD_REQUEST
            )

        if Ingredient.objects.filter(name=request.data["name"]).exists():
            return JsonResponse(
                {"status": "error", "message": "Ingredient name already exists"},
                status=HTTPStatus.BAD_REQUEST
            )

        try:
            Ingredient.objects.create(
                name=request.data["name"],
                preparation_time=request.data["preparation_time"],
                description=request.data["description"],
                category=category,
                magic_level=request.data["magic_level"]
            )
            return JsonResponse(
                {"status": "success", "message": "Ingredient created successfully"},
                status=HTTPStatus.CREATED
            )
        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": str(e)},
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )

class IngredientDetail(APIView):
    
    def get(self, request, id):
        try:
            ingredient = Ingredient.objects.get(id=id)
            data = {
                "id": ingredient.id,
                "name": ingredient.name,
                "slug": ingredient.slug,
                "description": ingredient.description,
                "magic_level": ingredient.magic_level,
                "preparation_time": ingredient.preparation_time,
                "category_id": ingredient.category.id,
                "category": ingredient.category.name,
                "date_created": DateFormat(ingredient.date_created).format('d/m/Y')
            }
            return JsonResponse({"data": data}, status=HTTPStatus.OK)
        except Ingredient.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Ingredient not found"},
                status=HTTPStatus.NOT_FOUND
            )
    
    def put(self, request, id):
        try:
            ingredient = Ingredient.objects.get(id=id)
        except Ingredient.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Ingredient not found"},
                status=HTTPStatus.NOT_FOUND
            )

        required_fields = ['name', 'preparation_time', 'description', 'category_id', 'magic_level']
        for field in required_fields:
            if not request.data.get(field):
                return JsonResponse(
                    {"status": "error", "message": f"The {field} field is required"},
                    status=HTTPStatus.BAD_REQUEST
                )

        try:
            category = Category.objects.get(pk=request.data["category_id"])
        except Category.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Invalid category ID"},
                status=HTTPStatus.BAD_REQUEST
            )

        if request.data["magic_level"] not in [choice[0] for choice in MAGIC_LEVEL_CHOICES]:
            return JsonResponse(
                {"status": "error", "message": "Invalid magic level value"},
                status=HTTPStatus.BAD_REQUEST
            )

        if Ingredient.objects.filter(name=request.data["name"]).exclude(id=id).exists():
            return JsonResponse(
                {"status": "error", "message": "Ingredient name already exists"},
                status=HTTPStatus.BAD_REQUEST
            )

        try:
            ingredient.name = request.data["name"]
            ingredient.preparation_time = request.data["preparation_time"]
            ingredient.description = request.data["description"]
            ingredient.category = category
            ingredient.magic_level = request.data["magic_level"]
            ingredient.save()
            return JsonResponse(
                {"status": "success", "message": "Ingredient updated successfully"},
                status=HTTPStatus.OK
            )
        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": str(e)},
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
    
    def delete(self, request, id):
        try:
            ingredient = Ingredient.objects.get(id=id)
            ingredient.delete()
            return JsonResponse(
                {"status": "success", "message": "Ingredient deleted successfully"},
                status=HTTPStatus.OK
            )
        except Ingredient.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Ingredient not found"},
                status=HTTPStatus.NOT_FOUND
            )
