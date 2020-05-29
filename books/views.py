from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from .filters import AuthorFilter, BookFilter


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    filterset_class = BookFilter
