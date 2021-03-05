# from django.test import TestCase

import pytest

from showtimes.models import Cinema, Screening
from .utils import fake_cinema_data
from movielist.tests.utils import fake_movie_data, create_fake_movie, fake_screening_data


@pytest.mark.django_db
def test_post_cinema(client, set_up):
    cinema_before = Cinema.objects.count()
    new_cinema = fake_cinema_data()
    response = client.post("/cinemas/", new_cinema, format='json')
    assert response.status_code == 201
    assert Cinema.objects.count() == cinema_before + 1
    for key, value in new_cinema.items():
        assert key in response.data
        assert response.data[key] == value
        # if isinstance(value, list):
        #     # Compare contents regardless of their order
        #     assert len(response.data[key]) == len(value)
        # else:
        #     assert response.data[key] == value


@pytest.mark.django_db
def test_get_cinema_list(client, set_up):
    response = client.get("/cinemas/", {}, format='json')

    assert response.status_code == 200
    assert Cinema.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_cinema_detail(client, set_up):
    cinema = Cinema.objects.first()
    response = client.get(f"/cinemas/{cinema.id}/", {}, format='json')

    assert response.status_code == 200
    for field in ("name", "city", "movies"):
        assert field in response.data


@pytest.mark.django_db
def test_delete_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.delete(f"/cinemas/{cinema.id}/", {}, format='json')
    assert response.status_code == 204
    cinema_ids = [cinema.id for cinema in Cinema.objects.all()]
    assert cinema.id not in cinema_ids


@pytest.mark.django_db
def test_update_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.get(f"/cinemas/{cinema.id}/", {}, format='json')
    cinema_data = response.data
    new_city = "BIAŁYSTOK"
    cinema_data["city"] = new_city
    response = client.patch(f"/cinemas/{cinema.id}/", cinema_data, format='json')
    assert response.status_code == 200
    cinema_obj = Cinema.objects.get(id=cinema.id)
    assert cinema_obj.city == new_city


@pytest.mark.django_db
def test_post_screeing(client, set_up):
    screening_before = Screening.objects.count()
    new_screening = fake_screening_data()
    response = client.post("/screening/", new_screening, format='json')
    # assert response.status_code == 201
    # assert Movie.objects.count() == movies_before + 1
    # for key, value in new_movie.items():
    #     assert key in response.data
    #     if isinstance(value, list):
    #         # Compare contents regardless of their order
    #         assert len(response.data[key]) == len(value)
    #     else:
    #         assert response.data[key] == value
