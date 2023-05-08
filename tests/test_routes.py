import pytest

def test_get_all_restaurants(client, two_restaurants):
    response = client.get("/restaurant")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Olive Garden",
            "cuisine": "Italian",
            "rating": 5,
            "distance_from_ada": 15
        },
        {   
            "id": 2,
            "name": "Texas Roadhouse",
            "cuisine": "American",
            "rating": 3,
            "distance_from_ada":3
        }
    ]

def test_post_creates_restaurant(client):
    response = client.post("/restaurant", json={ 
            "name": "Olive Garden",
            "cuisine": "Italian",
            "rating": 5,
            "distance_from_ada": 15
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body
    
def test_delete_restaurant(client, two_restaurants):
    response = client.delete("/restaurant/2")

    response_body = response.get_json()

    assert response.status_code == 200 
    assert "restaurant 2 successfully deleted" in response_body["msg"]
    
def test_put_restauarant(client, two_restaurants):
    response = client.put("/restaurant/1", json= {
            "name": "Hood Famous",
            "cuisine": "Filipino",
            "rating": 5,
            "distance_from_ada": 0
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"msg": "restaurant 1 successfully updated"}

