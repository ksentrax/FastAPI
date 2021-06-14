import json
import pytest

from app.api import crud


def test_create_organization(test_app, monkeypatch):
    request_payload = {
        "name": "Ford",
        "founded": 1913,
        "scope": "Automotive",
        "location": "Dearborn",
        "website": "ford.com",
    }
    response_payload = {
        "id": 1,
        "name": "Ford",
        "founded": 1913,
        "scope": "Automotive",
        "location": "Dearborn",
        "website": "ford.com",
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/organizations/",
                             data=json.dumps(request_payload))
    assert response.status_code == 201
    assert response.json() == response_payload


def test_create_organization_invalid_json(test_app):
    response = test_app.post("/organizations/",
                             data=json.dumps({"name": "Ford"}))
    assert response.status_code == 422


def test_read_organization(test_app, monkeypatch):
    test_data = {
        "id": 1,
        "name": "Ford",
        "founded": 1913,
        "scope": "Automotive",
        "location": "Dearborn",
        "website": "ford.com",
    }

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/organizations/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_organization_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/organizations/123")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"


def test_read_all_organizations(test_app, monkeypatch):
    test_data = [
        {"id": 1,
         "name": "Ford",
         "founded": 1913,
         "scope": "Automotive",
         "location": "Dearborn",
         "website": "www.ford.com",
         },
        {"id": 2,
         "name": "Intel",
         "founded": 1968,
         "scope": "Electronics",
         "location": "SantaClara",
         "website": "intel.com",
         }
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/organizations/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_update_organization(test_app, monkeypatch):
    test_update_data = {
        "id": 1,
        "name": "Ford",
        "founded": 1903,
        "scope": "Automotive",
        "location": "Dearborn",
        "website": "ford.com",
    }

    async def mock_get(id):
        return True

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/organizations/1/",
                            data=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data


@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"name": "Fard"}, 422],
    ],
)
def test_update_organization_invalid(test_app, monkeypatch, id,
                                     payload, status_code):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.put(f"/organizations/{id}/", data=json.dumps(payload))
    assert response.status_code == status_code


def test_remove_note(test_app, monkeypatch):
    test_data = {
        "id": 1,
        "name": "Ford",
        "founded": 1903,
        "scope": "Automotive",
        "location": "Dearborn",
        "website": "ford.com",
    }

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_delete(id):
        return id

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/organizations/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_remove_organization_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.delete("/organizations/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"
