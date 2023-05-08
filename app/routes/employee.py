from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.employee import Employee

employee_bp = Blueprint("employee", __name__, url_prefix = "/employee")

def validate_item(model, item_id):
    try:
        item_id = int(item_id)
    except ValueError:
        return abort(make_response({"message": f"invalid id: {item_id}"}, 400))
    
    return model.query.get_or_404(item_id)

@employee_bp.route("", methods =["POST"])
def add_restaurants():
    request_body = request.get_json()
    new_restaurant = Employee.from_dict(request_body)

    db.session.add(new_restaurant)
    db.session.commit()

    return make_response(jsonify({"id": new_restaurant.id}), 201)
    # return make_response(f"Book {new_book.title} successfully created", 201) 

@employee_bp.route("", methods=["GET"])
def get_restaurants():
    response = []
    name_query = request.args.get("name")
    if name_query is None:
        all_employees = Employee.query.all()
    else:
        all_employees = Employee.query.filter_by(name=name_query)
        
    for employee in all_employees:
        response.append(employee.to_dict())

    return make_response(jsonify(response), 200)

@employee_bp.route("/<emp_id>", methods = ["GET"])
def get_one_employee(emp_id):
    employee = validate_item(Employee, emp_id)
    # if restaurant is None:
    #     return {"message:" f"id {restaurant_id} not found"}, 404
    
    return make_response(jsonify(employee.to_dict()), 200)
    

@employee_bp.route("/<emp_id>", methods=["PUT"])
def update_employee(emp_id):
    employee = validate_item(Employee, emp_id)

    request_data = request.get_json()

    employee.name = request_data["name"]
    employee.salary = request_data["salary"]

    db.session.commit()

    return {"msg": f"restaurant {emp_id} successfully updated"}

@employee_bp.route("/<emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    employee = validate_item(Employee, emp_id)

    db.session.delete(employee)

    db.session.commit()

    return {"msg": f"restaurant {emp_id} successfully deleted"}, 200
