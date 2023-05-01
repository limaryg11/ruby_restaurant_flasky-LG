from flask import Blueprint, jsonify, request
from app import db
from app.models.restaurant import Restaurant

restaurant_bp = Blueprint("restaurant", __name__, url_prefix = "/restaurant")

@restaurant_bp.route("", methods =["POST"])
def add_restaurants():
    request_body = request.get_json()
    new_restaurant = Restaurant(
        rating = request_body["rating"],
        name = request_body["name"],
        cuisine = request_body["cuisine"],
        distance_from_ada = request_body["distance_from_ada"]
    )

    db.session.add(new_restaurant)
    db.session.commit()

    return {"id": new_restaurant.id}, 201
    # return make_response(f"Book {new_book.title} successfully created", 201) 

@restaurant_bp.route("", methods=["GET"])
def get_restaurants():
    response = []
    all_restaurants = Restaurant.query.all()
    for restaurant in all_restaurants:
        response.append(restaurant.to_dict())

    return jsonify(response), 200

# @restaurant_bp.route("/<id>", methods = ["GET"])
# def get_one_restaurant(id):
#     try:
#         restaurant_id = int(id)
#     except ValueError:
#         return {"message": f"invalid id: {id}"}, 400
    
#     for restaurant in restaurant_list:
#         if restaurant.id == restaurant_id:
#             return jsonify(restaurant.to_dict()), 200
    
#     return {"message:" f"id {restaurant_id} not found"}, 404
    

