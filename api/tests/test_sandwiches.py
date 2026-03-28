from fastapi.testclient import TestClient
from ..controllers import sandwiches
from ..main import app
import pytest
from ..models import models

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_sandwich(db_session):
    sandwich_data = {
        "sandwich_name": "Club Sandwich",
        "price": 8.50
    }

    sandwich_object = models.Sandwich(**sandwich_data)

    created_sandwich = sandwiches.create(db_session, sandwich_object)

    assert created_sandwich is not None
    assert created_sandwich.sandwich_name == "Club Sandwich"
    assert created_sandwich.price == 8.50