from django.urls import path
from .views import *

urlpatterns = [
    path('ingredients', Class1.as_view()),
    path('ingredients/<int:id>', Class2.as_view())
]