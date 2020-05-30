from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from .serializers import AuthorSerializer, BookSerializer, BookReadSerializer
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

    def list(self, request):
        queryset = Book.objects.all().order_by('name')
        serializer = BookReadSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        serializer = BookReadSerializer(book)
        return Response(serializer.data)
