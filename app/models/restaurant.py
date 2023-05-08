from app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(db.Integer)
    name = db.Column(db.String)
    cuisine = db.Column(db.String)
    distance_from_ada = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "name": self.name,
            "cuisine": self.cuisine,
            "distance_from_ada": self.distance_from_ada
        }
    @classmethod
    def from_dict(cls, restaurant_data):
        return cls(
            name = restaurant_data["name"],
            rating = restaurant_data["rating"],
            cuisine = restaurant_data["cuisine"],
            distance_from_ada = restaurant_data["distance_from_ada"]
        )