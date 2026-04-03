from flask import Blueprint, request, jsonify
from models.student import students

student_bp = Blueprint("student", __name__)

# CREATE
@student_bp.route("/students", methods=["POST"])
def add_student():
    data = request.json
    students.append(data)
    return jsonify({"message": "Student added"}), 201

# READ
@student_bp.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# UPDATE
@student_bp.route("/students/<int:index>", methods=["PUT"])
def update_student(index):
    if index < len(students):
        students[index] = request.json
        return jsonify({"message": "Student updated"})
    return jsonify({"error": "Not found"}), 404

# DELETE
@student_bp.route("/students/<int:index>", methods=["DELETE"])
def delete_student(index):
    if index < len(students):
        students.pop(index)
        return jsonify({"message": "Deleted"})
    return jsonify({"error": "Not found"}), 404
