from rest_framework.reverse import reverse

import pytest

pytestmark = pytest.mark.django_db

def test_author_response(client):
    response = client.get(reverse("authors"))
    assert response.status_code == 200