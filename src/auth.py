from flask import request, jsonify
from functools import wraps

API_KEY = "mysecretkey123"

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get("x-api-key")

        if not key or key != API_KEY:
            return jsonify({
                "message": "Unauthorized. Invalid or missing API key."
            }), 401

        return f(*args, **kwargs)

    return decorated