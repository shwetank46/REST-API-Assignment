from flask import Blueprint, request, jsonify
from src import db
from src.models.base import Record
from src.auth import require_api_key

# Create Blueprint
api_bp = Blueprint("api", __name__)


def _validate_record_payload(payload, required_fields=None):
    if payload is None:
        return False, "Request body must be JSON"

    if required_fields:
        missing = [field for field in required_fields if field not in payload]
        if missing:
            return False, f"Missing required fields: {', '.join(missing)}"

    return True, None


# ------------------------------
# Add Record
# ------------------------------

@api_bp.route("/records", methods=["POST"])
@require_api_key
def add_record():
    """
    Create a new record
    ---
    tags:
      - Records
    consumes:
      - application/json
    parameters:
      - name: x-api-key
        in: header
        type: string
        required: true
        description: API Key
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            category:
              type: string
            status:
              type: string
          required:
            - name
            - category
            - status
    responses:
      201:
        description: Record created successfully
      400:
        description: Invalid request payload
      401:
        description: Invalid or missing API key
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        valid, error = _validate_record_payload(data, ["name", "category", "status"])
        if not valid:
            return jsonify({"error": error}), 400

        record = Record(
            name=data["name"].strip(),
            category=data["category"].strip(),
            status=data["status"].strip(),
        )

        db.session.add(record)
        db.session.commit()

        return jsonify({
            "message": "Record added successfully",
            "data": record.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# ------------------------------
# Get Records
# ------------------------------

@api_bp.route("/records", methods=["GET"])
@require_api_key
def get_records():
    """
    Retrieve all records
    ---
    tags:
      - Records
    parameters:
      - name: category
        in: query
        type: string
        required: false
        description: Filter records by category
      - name: status
        in: query
        type: string
        required: false
        description: Filter records by status
      - name: x-api-key
        in: header
        type: string
        required: true
        description: API Key
    responses:
      200:
        description: List of records returned successfully
      401:
        description: Invalid or missing API key
      500:
        description: Internal server error
    """
    try:
        category = request.args.get("category")
        status = request.args.get("status")

        query = Record.query
        if category:
            query = query.filter_by(category=category)
        if status:
            query = query.filter_by(status=status)

        records = query.all()
        return jsonify([r.to_dict() for r in records])

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------
# Update Record
# ------------------------------

@api_bp.route("/records/<int:id>", methods=["PUT"])
@require_api_key
def update_record(id):
    """
    Update a record
    ---
    tags:
      - Records
    consumes:
      - application/json
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the record to update
      - name: x-api-key
        in: header
        type: string
        required: true
        description: API Key
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            category:
              type: string
            status:
              type: string
    responses:
      200:
        description: Record updated successfully
      400:
        description: Invalid request payload
      401:
        description: Invalid or missing API key
      404:
        description: Record not found
      500:
        description: Internal server error
    """
    try:
        record = Record.query.get(id)
        if not record:
            return jsonify({"error": "Record not found"}), 404

        data = request.get_json()
        valid, error = _validate_record_payload(data)
        if not valid:
            return jsonify({"error": error}), 400

        record.name = data.get("name", record.name).strip()
        record.category = data.get("category", record.category).strip()
        record.status = data.get("status", record.status).strip()

        db.session.commit()
        return jsonify({"message": "Record updated", "data": record.to_dict()}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# ------------------------------
# Delete Record
# ------------------------------

@api_bp.route("/records/<int:id>", methods=["DELETE"])
@require_api_key
def delete_record(id):
    """
    Delete a record
    ---
    tags:
      - Records
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the record to delete
      - name: x-api-key
        in: header
        type: string
        required: true
        description: API Key
    responses:
      200:
        description: Record deleted successfully
      401:
        description: Invalid or missing API key
      404:
        description: Record not found
      500:
        description: Internal server error
    """
    try:
        record = Record.query.get(id)
        if not record:
            return jsonify({"error": "Record not found"}), 404

        db.session.delete(record)
        db.session.commit()
        return jsonify({"message": "Record deleted"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
