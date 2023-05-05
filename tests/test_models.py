import pytest
from app.models.planet import Planet

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(
        id = 1,
        name="Mercury",
        description="First planet from the sun",
        moon_count=0
    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "First planet from the sun"
    assert result["moon_count"] == 0

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(
        name="Mercury", 
        description="First planet from the sun",
        moon_count=0
    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mercury"
    assert result["description"] == "First planet from the sun"
    assert result["moon_count"] == 0

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1, description="First planet", moon_count=0)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "First planet"
    assert result["moon_count"] == 0

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(
        id = 1,
        name="Mercury",
        moon_count=0
    )

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] is None
    assert result["moon_count"] == 0

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "New Planet",
        "description": "The Best!",
        "moon_count": 234
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The Best!"
    assert new_planet.moon_count == 234

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "The Best!",
        "moon_count": 234
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "New Planet",
        "moon_count": 234
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "New Planet",
        "description": "The Best!",
        "moon_count": 234,
        "another": "last value"
    }
    
    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The Best!"
    assert new_planet.moon_count == 234