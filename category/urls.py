from django.urls import path, include
from .views import *

urlpatterns = [
    path('category/', ClassName.as_view()),
]