def test_get_all_potential_recruits(client):
    response = client.get("/potential_recruits/")
    assert response.status_code == 200
    recruits = response.json()
    assert isinstance(recruits, list)

def test_search_potential_recruits(client):
    response = client.get("/potential_recruits/search/?keyword=Michael")
    assert response.status_code == 200
    results = response.json()
    assert any("michaelnathan@gmail.com" in r["email"] for r in results)
