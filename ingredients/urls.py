from django.urls import path
from .views import *

urlpatterns = [
    path('ingredients', Clase1.as_view()),
    path('ingredients/<int:id>', Clase2.as_view())
]