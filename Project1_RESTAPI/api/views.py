from django.shortcuts import render
from rest_framework.response import Response 
from .models import BlogPost 
from .serializers import BlogPostSerializers 
from rest_framework import generics 
# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all() 
    serializer_class = BlogPostSerializers 

