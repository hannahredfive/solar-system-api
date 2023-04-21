from flask import Blueprint, jsonify, abort, make_response

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

class Planet():
    def __init__(self, id, name, description, moon_count):
        self.id = id
        self.name = name
        self.description = description
        self.moon_count = moon_count

planets = [
    Planet(1, "Mercury", "Closest planet to the sun, has no atmosphere, and revolves around the sun faster than any other planet in our Solar System.", 0),
    Planet(2, "Venus", "Second closest planet to the sun, is the only planet in our Solar System besides Earth that has a substantial atmosphere.", 0),
    Planet(3, "Earth", "Third from the Sun and the only known place in the universe where life has originated and found habitability.", 1),
    Planet(4, "Mars", "Fourth planet from the Sun and the third largest and massive terrestrial object in the Solar System.", 2),
    Planet(5, "Jupiter", " Jupiter is more than twice as massive than the other planets of our solar system combined. The giant planet's Great Red Spot is a centuries-old storm bigger than Earth.", 95),
    Planet(6, "Saturn", "Adorned with a dazzling, complex system of icy rings, Saturn is unique in our solar system. The other giant planets have rings, but none are as spectacular as Saturn's.", 83),
    Planet(7, "Uranus", "Uranus—seventh planet from the Sun—rotates at a nearly 90-degree angle from the plane of its orbit. This unique tilt makes Uranus appear to spin on its side.", 27),
    Planet(8, "Neptune", "Neptune—the eighth and most distant major planet orbiting our Sun—is dark, cold and whipped by supersonic winds. It was the first planet located through mathematical calculations.", 14)
]


'''ENDPOINTS/ROUTES BELOW'''

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "number of moons": planet.moon_count
        })
    return jsonify(planets_response)


# wave 2, handles existing planet & invalid planet 400 & non-existing planet 404
@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"msg":f"planet {planet_id} invalid"}, 400
    
    for planet in planets:
        if planet.id == planet_id:
            return jsonify({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "number of moons": planet.moon_count
            })
        
    return {"msg": f"planet {planet_id} not found"}, 404


# refactored handle_planets by created helper func

