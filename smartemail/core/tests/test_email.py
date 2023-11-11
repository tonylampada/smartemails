from unittest.mock import ANY

from smartemail.accounts.models import User
from smartemail.accounts.tests import fixtures
from smartemail.core.models import Emai


def test_criar_emai_sem_login(client):
    resp = client.post("/api/core/email/add", {"new_emai": "walk the dog"})
    assert resp.status_code == 401


def test_criar_emai_com_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    payload = {"description": "estudar pytest"}
    resp = client.post("/api/core/email/add", payload, content_type="application/json")
    assert resp.status_code == 200


def test_listar_emai_com_login(client, db):
    fixtures.user_jon()
    Emai.objects.create(description="walk the dog")

    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/core/email/list")
    data = resp.json()

    assert resp.status_code == 200
    assert data == {
        "email": [{"description": "walk the dog", "done": False, "id": ANY}]
    }
