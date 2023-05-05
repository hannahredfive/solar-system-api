from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moon_count = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moon_count": self.moon_count
        }
    
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(
            name=planet_data["name"], 
            description=planet_data["description"],
            moon_count=planet_data["moon_count"]
        )
        return new_planet