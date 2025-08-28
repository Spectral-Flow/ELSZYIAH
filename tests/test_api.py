import sys

import pytest
from fastapi.testclient import TestClient

sys.path.append("backend")
from backend.elysia_lite import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    data = r.json()
    assert "service" in data
    assert data["service"].startswith("Elysia Concierge")


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "healthy"
    assert "mode" in data


def test_amenities():
    r = client.get("/api/elysia/amenities")
    assert r.status_code == 200
    data = r.json()
    assert "amenities" in data
    assert isinstance(data["amenities"], list)


def test_submit_request_maintenance():
    payload = {
        "resident_id": "TEST-1",
        "unit_number": "101",
        "request_type": "maintenance",
        "message": "My sink is leaking",
        "priority": "medium",
    }
    r = client.post("/api/elysia/request", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "response" in data
    assert "request_id" in data
