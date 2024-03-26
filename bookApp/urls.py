from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailBook.as_view()),
    path('create/', CreateBook.as_view()),
    path('delete/<int:pk>/', DeleteBook.as_view()),
    path('', ListBook.as_view()),
]