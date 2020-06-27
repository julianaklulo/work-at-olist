from rest_framework.reverse import reverse
from books.models import Author, Book

import pytest

pytestmark = pytest.mark.django_db


def test_author_list(client):
    response = client.get(reverse("authors-list"))
    assert response.status_code == 200


def test_author_create(client):
    client.post(reverse("authors-list"), {"name": "Juliana"})
    assert len(Author.objects.all()) == 1


def test_book_list(client):
    response = client.get(reverse("books-list"))
    assert response.status_code == 200


def test_book_create(client):
    response = client.post(reverse("authors-list"), {"name": "Author 1"})
    author_id = response.data["id"]

    client.post(reverse("books-list"), {
        "name": "Book",
        "publication_year": 2020,
        "edition": "1",
        "authors": author_id
    })
    assert len(Book.objects.all()) == 1


def test_book_read(client):
    response = client.post(reverse("authors-list"), {"name": "Author 1"})
    author_id = response.data["id"]

    response = client.post(reverse("books-list"), {
        "name": "Book 1",
        "publication_year": 2020,
        "edition": "1",
        "authors": author_id
    })
    book_id = response.data["id"]

    response = client.get(reverse("books-detail", kwargs={"pk": book_id}))
    assert response.data["name"] == "Book 1"
    assert response.data["publication_year"] == 2020
    assert response.data["edition"] == "1"
    assert response.data["authors"][0] == author_id


def test_book_update(client):
    response = client.post(reverse("authors-list"), {"name": "Author 1"})
    author_id = response.data["id"]

    response = client.post(reverse("books-list"), {
        "name": "Book 1",
        "publication_year": 2020,
        "edition": "1",
        "authors": author_id
    })
    book_id = response.data["id"]

    response = client.patch(reverse("books-detail", kwargs={"pk": book_id}), {
        "name": "Book 2"
    })

    assert response.data["name"] == "Book 2"


def test_book_delete(client):
    response = client.post(reverse("authors-list"), {"name": "Author 1"})
    author_id = response.data["id"]

    response = client.post(reverse("books-list"), {
        "name": "Book 1",
        "publication_year": 2020,
        "edition": "1",
        "authors": author_id
    })
    book_id = response.data["id"]

    response = client.delete(reverse("books-detail", kwargs={"pk": book_id}))

    assert response.status_code == 204
    assert len(Book.objects.filter(id=book_id)) == 0
