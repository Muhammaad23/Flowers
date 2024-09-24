from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Book
from .serializer import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()  # Fixed typo from Book.object.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ["id", "name"]
