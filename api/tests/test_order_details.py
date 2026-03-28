from fastapi.testclient import TestClient
from ..controllers import order_details
from ..main import app
import pytest
from ..models import models

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_order_detail(db_session):
    order_detail_data = {
        "order_id": 1,
        "sandwich_id": 2,
        "amount": 3
    }

    order_detail_object = models.OrderDetail(**order_detail_data)

    created_detail = order_details.create(db_session, order_detail_object)

    assert created_detail is not None
    assert created_detail.order_id == 1
    assert created_detail.sandwich_id == 2
    assert created_detail.amount == 3