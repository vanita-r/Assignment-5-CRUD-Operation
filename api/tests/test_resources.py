from fastapi.testclient import TestClient
from ..controllers import resources
from ..main import app
import pytest
from ..models import models

client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_resource(db_session):
    resource_data = {
        "item_name": "Sourdough Bread",
        "amount": 50
    }

    resource_object = models.Resource(**resource_data)

    created_resource = resources.create(db_session, resource_object)

    assert created_resource is not None
    assert created_resource.item_name == "Sourdough Bread"
    assert created_resource.amount == 50


def test_read_all_resources(db_session, mocker):
    mock_resources = [
        models.Resource(item_name="Ham", amount=20),
        models.Resource(item_name="Cheese", amount=30)
    ]

    db_session.query.return_value.all.return_value = mock_resources

    all_resources = resources.read_all(db_session)

    assert len(all_resources) == 2
    assert all_resources[0].item_name == "Ham"