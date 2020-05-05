from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=150)
    publication_year = models.PositiveSmallIntegerField()
    edition = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name
