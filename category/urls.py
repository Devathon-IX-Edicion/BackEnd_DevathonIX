from django.urls import path, include
from .views import *

urlpatterns = [
    path('category/', Class1.as_view()),
    path('category/<int:id>', Class2.as_view()),
]