from rest_framework.views import APIView
from .models import *
from django.http.response import JsonResponse
from rest_framework.response import Response
from .serializers import *
from http import HTTPStatus


class ClassName(APIView):
    def get(self, request):
        # SELECT * from  category order by desc:
        data = Category.objects.order_by('-id').all()
        json_data =  CategorySerializer(data, many=True)
        #return Response(date_json.data)
        return  JsonResponse({"data":json_data.data}, HTTPStatus.OK)