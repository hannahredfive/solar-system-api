from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# helper functions
def validate_planet(planet_id):
    try: 
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet


'''ENDPOINTS/ROUTES BELOW'''

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)


@planets_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter(Planet.name.ilike(name_query))

    else:
        planets = Planet.query.all()
    
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    
    return jsonify(planets_response), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict(), 200


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moon_count = request_body["moon_count"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated", 200)


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted", 200)