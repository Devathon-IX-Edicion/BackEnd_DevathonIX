from rest_framework.views import APIView
from .models import *
from django.http.response import JsonResponse
from rest_framework.response import Response
from .serializers import *
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify
from recetas.models import *

class Clase1(APIView):
    def get(self, request):
        data = Categoria.objects.order_by('-id').all()
        datos_json = CategoriaSerializer(data, many=True)
        return JsonResponse({"data":datos_json.data}, status=HTTPStatus.OK)
        
    def post(self, request):
        if request.data.get("name")==None or not request.data['name']:
            return JsonResponse({"status":"error", "message":"El campo nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        try:
            Categoria.objects.create(name=request.data['name'])
            return JsonResponse({"status":"ok", "message":"Se crea el registro exitosamente"}, status=HTTPStatus.CREATED)
        except Exception as e:
            raise Http404

class Clase2(APIView):
    def get(self, request, id):
        try:
            data = Categoria.objects.filter(id=id).get()
            return JsonResponse({"data": {"id":data.id, "name":data.name, "slug":data.slug}}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
    
    def put(self, request, id):
        if request.data.get("name")==None:
            return JsonResponse({"status":"error", "message":"El campo name es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        if not request.data.get("name"):
            return JsonResponse({"status":"error", "message":"El campo name es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        try:
            data = Categoria.objects.filter(pk=id).get()
            Categoria.objects.filter(pk=id).update(name=request.data.get("name"), slug=slugify(request.data.get("name")))
            return JsonResponse({"estado":"ok", "message":"Se modifica el registro exitosamente"}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
        
    def delete(self, request, id):
        try:
            data = Categoria.objects.filter(pk=id).get()
        except Categoria.DoesNotExist:
            raise Http404
        if Receta.objects.filter(categoria_id=id).exists():
            return JsonResponse({"status":"error", "message":"Ocurrió un error inesperado"}, status=HTTPStatus.BAD_REQUEST)
        Categoria.objects.filter(pk=id).delete()
        return JsonResponse({"status":"ok", "message":"Se elimina el registro exitosamente"}, status=HTTPStatus.OK)