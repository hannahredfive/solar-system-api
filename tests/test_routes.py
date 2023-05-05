import pytest

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

def test_get_one_planet_id_not_found(client, two_saved_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"Planet 3 not found"}

def test_get_one_planet_id_invalid(client, two_saved_planets):
    # Act
    response = client.get("/planets/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message":"Planet cat invalid"}

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

def test_create_one_planet_no_name(client):
    # Arrange
    test_data = {"description": "The Best!"}

    # Act & Assert
    with pytest.raises(KeyError, match='name'):
        response = client.post("/planets", json=test_data)

def test_create_one_planet_no_description(client):
    # Arrange
    test_data = {"name": "New planet"}

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        response = client.post("/planets", json=test_data)

def test_create_one_planet_with_extra_keys(client, two_saved_planets):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "New planet",
        "description": "The Best!",
        "moon_count": 234,
        "another": "last value"
    }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet New planet successfully created"