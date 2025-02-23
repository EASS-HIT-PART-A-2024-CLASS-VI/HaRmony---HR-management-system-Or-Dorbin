def test_get_all_employees(client):
    response = client.get("/Employees/")
    assert response.status_code == 200
    employees = response.json()
    assert isinstance(employees, list)
    assert any(e["email"] == "john.doe@example.com" for e in employees)

def test_search_employees(client):
    response = client.get("/Employees/search/?name=Rachel")
    assert response.status_code == 200
    results = response.json()
    assert any(r["email"] == "rachel@gmail.com" for r in results)
