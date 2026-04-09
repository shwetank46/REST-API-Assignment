def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary.")
    
    required_fields = ['name', 'category', 'status']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    
    return True

def format_response(data, status_code=200):
    return {
        "status": "success" if status_code < 400 else "error",
        "data": data,
        "status_code": status_code
    }