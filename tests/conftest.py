import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client() 

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mercury_planet = Planet(
        name="Mercury", 
        description="First planet from the sun", 
        moon_count=0
    )
    earth_planet = Planet(
        name="Earth", 
        description="Third planet from the sun", 
        moon_count=1
    )

    # db.session.add_all([mercury_planet, earth_planet])
    # Alternatively, we could do
    db.session.add(mercury_planet)
    db.session.add(earth_planet)
    db.session.commit()

