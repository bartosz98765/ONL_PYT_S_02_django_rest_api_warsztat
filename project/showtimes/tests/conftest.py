import os
import sys

import pytest
from rest_framework.test import APIClient

from .utils import create_fake_cinema
from movielist.tests.utils import create_fake_movie

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for _ in range(8):
        create_fake_movie()
    for _ in range(3):
        create_fake_cinema()
