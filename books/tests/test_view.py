from rest_framework.reverse import reverse
from books.models import Author, Book

import pytest


pytestmark = pytest.mark.django_db


def test_author_list(client):
    response = client.get(reverse("authors-list"))
    assert response.status_code == 200


def test_author_create(client):
    client.post(reverse("authors-list"), {"name": "Author"})
    assert len(Author.objects.all()) == 1


def test_author_search(client):
    client.post(reverse("authors-list"), {"name": "Author 42"})

    response = client.get(reverse("authors-list"), {"name": "42"})
    assert response.data["results"][0]["name"] == "Author 42"


def test_author_pagination(client):
    for i in range(15):
        client.post(reverse("authors-list"), {"name": f"Author #{i}"})
    response = client.get(reverse("authors-list"))
    assert response.data["count"] == 15
    assert len(response.data["results"]) == 10
    assert response.data["next"] != "null"


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
    }, content_type='application/json')

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


def test_book_search(client):
    response = client.post(reverse("authors-list"), {"name": "Very Good Author"})
    author_id = response.data["id"]

    response = client.post(reverse("books-list"), {
        "name": "Book 1",
        "publication_year": 2020,
        "edition": "1",
        "authors": author_id
    })

    response = client.post(reverse("books-list"), {
        "name": "Book 2",
        "publication_year": 2002,
        "edition": "2",
        "authors": author_id
    })
    
    response = client.get(reverse("books-list"), {"name": "2"})
    for book in response.data["results"]:
        assert "2" in book["name"]
    
    response = client.get(reverse("books-list"), {"publication_year": 2020})
    for book in response.data["results"]:
        assert book["publication_year"] == 2020

    response = client.get(reverse("books-list"), {"edition": "1"})
    for book in response.data["results"]:
        assert "1" in book["edition"]

    response = client.get(reverse("books-list"), {"authors__name": "Very Good Author"})
    for book in response.data["results"]:
        assert book["authors"] == [author_id]

    response = client.get(reverse("books-list"), {
        "name": "Book 1",
        "publication_year": 2020,
        "edition": "1",
        "authors__name": "Very Good Author"})
    for book in response.data["results"]:
        assert book["name"] == "Book 1"
        assert book["publication_year"] == 2020
        assert book["edition"] == "1"
        assert book["authors"] == [author_id]
