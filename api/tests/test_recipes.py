from fastapi.testclient import TestClient
from ..controllers import recipes
from ..main import app
import pytest
from ..models import models

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_recipe(db_session):
    recipe_data = {
        "sandwich_id": 1,
        "resource_id": 2,
        "amount": 5.0
    }

    recipe_object = models.Recipe(**recipe_data)

    created_recipe = recipes.create(db_session, recipe_object)

    assert created_recipe is not None
    assert created_recipe.sandwich_id == 1
    assert created_recipe.resource_id == 2
    assert created_recipe.amount == 5.0