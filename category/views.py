from rest_framework.views import APIView
from .models import *
from django.http.response import JsonResponse
from rest_framework.response import Response
from .serializers import *
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify

class Class1(APIView):
    def get(self, request):
        data = Category.objects.order_by('-id').all()
        json_data = CategorySerializer(data, many=True)
        return Response(
            {"data": json_data.data},
            status=HTTPStatus.OK
        )

    def post(self, request):
        if request.data.get("name") is None or not request.data["name"]:
            return JsonResponse(
                {"status": "error", "message": "The row field 'name' is obligatory"},
                status=HTTPStatus.BAD_REQUEST
            )
        try:
            Category.objects.create(name=request.data["name"])

            return JsonResponse(
                {"status": "ok", "message": "The register was created successfully"},
                status=HTTPStatus.CREATED
            )
        except Exception as e:
            return JsonResponse(
                {"status": "Something went wrong", "details": str(e)},
                status=HTTPStatus.BAD_REQUEST
            )

class Class2(APIView):
    def get(self, request, id):
        try:
            data = Category.objects.get(id=id) 
            return JsonResponse(
                {
                    "data": {
                        "id": data.id,
                        "name": data.name,
                        "slug": data.slug
                    }
                },
                status=HTTPStatus.OK
            )
        except Category.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Category not found"},
                status=HTTPStatus.NOT_FOUND
            )

    def put(self, request, id):
        if not request.data.get("name"):
            return JsonResponse(
                {"status": "error", "message": "The field 'name' is obligatory"},
                status=HTTPStatus.BAD_REQUEST
            )

        try:
            data = Category.objects.get(pk=id)
            data.name = request.data.get("name")
            data.slug = slugify(request.data.get("name"))
            data.save()

            return JsonResponse(
                {"status": "ok", "message": "The register was updated successfully"},
                status=HTTPStatus.OK
            )

        except Category.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Category not found"},
                status=HTTPStatus.NOT_FOUND
            )
        except Exception as e:
            return JsonResponse(
                {"error": "Something went wrong", "details": str(e)},
                status=HTTPStatus.BAD_REQUEST
            )
    
    def delete(self, request, id):
        try:
            data = Category.objects.get(pk=id)
            data.delete()

            return JsonResponse(
                {"status": "ok", "message": "The register was deleted successfully"},
                status=HTTPStatus.OK
            )

        except Category.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Category not found"},
                status=HTTPStatus.NOT_FOUND
            )
        except Exception as e:
            return JsonResponse(
                {"error": "Something went wrong", "details": str(e)},
                status=HTTPStatus.BAD_REQUEST
            )