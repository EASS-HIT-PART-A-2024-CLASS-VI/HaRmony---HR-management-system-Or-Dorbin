def test_register_and_login(client):
    response = client.post("/auth/register/", json={
        "username": "testuser",
        "password": "testpass",
        "role": "testrole",
        "company": "testcompany"
    })
    assert response.status_code in [200, 400]  

    response = client.post("/auth/login/", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}
