from app import db

class Employee (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    salary = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"))
    restaurant = db.relationship("Restaurant", back_populates="employees")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "salary": self.salary,
        }
    @classmethod
    def from_dict(cls, employee_data):
        return cls(
            name = employee_data["name"],
            salary= employee_data["salary"],
        )