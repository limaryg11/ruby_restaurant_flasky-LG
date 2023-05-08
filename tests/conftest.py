import pytest
from app import create_app, db
from app.models.restaurant import Restaurant
from flask.signals import request_finished

@pytest.fixture
def app():
    app = create_app(True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_restaurants():
    olivegarden = Restaurant(name="Olive Garden", cuisine="Italian", rating=5, distance_from_ada=15)
    texasroadhouse = Restaurant(name="Texas Roadhouse", cuisine="American", rating=3, distance_from_ada=3)

    db.session.add_all([olivegarden, texasroadhouse])
    db.session.commit()