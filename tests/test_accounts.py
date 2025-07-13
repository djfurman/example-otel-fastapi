from fastapi.testclient import TestClient


def test_endpoint_for_get_accounts_collection(test_client: TestClient) -> None:
    response = test_client.get("/accounts")
    assert response.status_code == 200

    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) > 0


def test_endpoint_for_get_account_by_id(test_client: TestClient) -> None:
    response = test_client.get("/accounts/abc123")
    assert response.status_code == 200

    response_data = response.json()
    assert isinstance(response_data, dict)
    assert response_data["id"] == "abc123"
    assert response_data["balance"] == -500
    assert response_data["is_current"]
