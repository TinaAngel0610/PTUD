from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailBlog.as_view()),
    path('create/', CreateBlog.as_view()),
    path('delete/<int:pk>/', DeleteBlog.as_view()),
    path('', ListBlog.as_view()),
]