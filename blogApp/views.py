from django.shortcuts import render
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.
class ListBlog(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class DetailBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class CreateBlog(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer   
    
class DeleteBlog(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer