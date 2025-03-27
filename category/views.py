from rest_framework.views import APIView
from django.http.response import JsonResponse


class ClassName(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})