import pytest
import types
import json

from backend.elysia_lite import HostedBloomAI, ResidentRequest, RequestType

class DummyResponse:
    def __init__(self, json_data):
        self._json = json_data
    def json(self):
        return self._json
    def raise_for_status(self):
        return None


def fake_post(url, headers=None, json=None, timeout=60):
    # simulate HF returning a list of dicts with generated_text
    return DummyResponse([{"generated_text": "Hello from hosted HF adapter."}])


def test_hosted_adapter_monkeypatch(monkeypatch):
    monkeypatch.setattr('requests.post', fake_post)

    api_key = 'fake-key'
    model = 'fake/model'
    adapter = HostedBloomAI(api_key, model)

    req = ResidentRequest(resident_id='T1', unit_number='100', request_type=RequestType.GENERAL_INQUIRY, message='Hello')

    # run the coroutine
    import asyncio
    result = asyncio.get_event_loop().run_until_complete(adapter.generate_response(req))
    assert 'Hello from hosted HF adapter' in result
