# get all planets and return no records
def test_get_all_planets_with_no_records(client):
    # ARRANGE is inside Conftest
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [] 

def test_get_all_planets_with_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Mercury",
            "description": "First planet from the sun",
            "moon_count": 0
        },
        {
            "id": 2,
            "name": "Earth",
            "description": "Third planet from the sun",
            "moon_count": 1
        }
    ]

def test_get_all_planets_with_name_query_no_match(client, two_saved_planets):
    # Act
    data = {"name": "Pluto"}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_records_and_query_param_matching_returns_planet(client, two_saved_planets):
    # Act
    data = {"name": "Mercury"}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Mercury",
            "description": "First planet from the sun",
            "moon_count": 0
        }
    ]

# get one planet by id
def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "description": "First planet from the sun",
        "id": 1,
        "moon_count": 0,
        "name": "Mercury"
    }

# create one planet, returns success msg
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "description": "First planet from the sun",
        "moon_count": 0,
        "name": "Mercury"
    })

    response_body = response.get_json()
    # response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Mercury successfully created"

