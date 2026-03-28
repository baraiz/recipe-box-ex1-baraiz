def test_create_recipe(client):
    """Creating a recipe returns 201 with normalized payload."""
    response = client.post(
        "/recipes",
        json={"title": "Banana and Chocolate Chip Cake", "prep_time": 45, "category": "cakes"},
    )
    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["category"] == "Cakes"

def test_list_recipes(client):
    """Can retrieve recipes after creating them."""
    client.post("/recipes", json={"title": "Samosa", "prep_time": 90, "category": "pastries"})
    response = client.get("/recipes")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Samosa"

def test_get_missing_recipe_returns_404(client):
    """Requesting non-existent recipe returns 404."""
    response = client.get("/recipes/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Recipe not found"

def test_delete_recipe(client):
    """Can delete a recipe and it's gone afterwards."""
    create_response = client.post(
        "/recipes",
        json={"title": "Quick Bread", "prep_time": 60, "category": "breads"},
    )
    recipe_id = create_response.json()["id"]
    
    response = client.delete(f"/recipes/{recipe_id}")
    assert response.status_code == 204
    
    assert client.get(f"/recipes/{recipe_id}").status_code == 404
