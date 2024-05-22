def test_access_invalid_api(client, h_principal):
    response = client.get("/invalid-api", headers=h_principal)

    assert response.status_code == 404

    error_response = response.json

    assert error_response["error"] == "NotFound"
