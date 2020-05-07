from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
