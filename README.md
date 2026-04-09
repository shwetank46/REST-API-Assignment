# Records API - REST API Assignment

## Project Overview

**Records API** is a Flask-based REST API designed for managing records with full CRUD operations. The API provides comprehensive documentation through Swagger/OpenAPI and implements secure API key authentication for all endpoints.

### Key Features
- **CRUD Operations**: Create, Read, Update, and Delete records
- **Filtering Capabilities**: Filter records by category and status
- **API Key Authentication**: Secure endpoints with x-api-key header authentication
- **Swagger Documentation**: Interactive API documentation at `/apidocs`
- **SQLite Database**: Lightweight, file-based database for data persistence
- **Error Handling**: Comprehensive error responses with appropriate HTTP status codes
- **Input Validation**: Automatic validation of request payloads

---

## Local Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment support (venv)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/rest-api-assignment.git
   cd rest-api-assignment
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

4. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

   The server will start on `http://127.0.0.1:5000`

---

## Testing Environment

### Local Development
- **Base URL**: `http://127.0.0.1:5000`
- **API Documentation**: `http://127.0.0.1:5000/apidocs`
- **Database**: SQLite (`instance/database.db`)

### Testing Endpoints

All requests must include the API key header for authentication.

#### Example: GET All Records
```bash
curl -X GET "http://127.0.0.1:5000/records" \
  -H "x-api-key: mysecretkey123"
```

#### Example: Create a Record
```bash
curl -X POST "http://127.0.0.1:5000/records" \
  -H "x-api-key: mysecretkey123" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sample Record",
    "category": "test",
    "status": "active"
  }'
```

#### Example: Filter Records by Category
```bash
curl -X GET "http://127.0.0.1:5000/records?category=test" \
  -H "x-api-key: mysecretkey123"
```

#### Example: Update a Record
```bash
curl -X PUT "http://127.0.0.1:5000/records/1" \
  -H "x-api-key: mysecretkey123" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Record",
    "category": "updated",
    "status": "inactive"
  }'
```

#### Example: Delete a Record
```bash
curl -X DELETE "http://127.0.0.1:5000/records/1" \
  -H "x-api-key: mysecretkey123"
```

---

## API Authentication

### Authentication Method
The API uses **API Key authentication** through the `x-api-key` header.

### Authentication Header
All API requests must include:
```
x-api-key: mysecretkey123
```

### Local Testing Authentication Key
```
mysecretkey123
```

### Error Response (Missing/Invalid Key)
```json
{
  "message": "Unauthorized. Invalid or missing API key."
}
```

**HTTP Status Code**: `401 Unauthorized`

---

## API Endpoints

### Records Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/records` | Create a new record |
| GET | `/records` | Retrieve all records (with optional filtering) |
| GET | `/records?category=value` | Filter records by category |
| GET | `/records?status=value` | Filter records by status |
| PUT | `/records/<id>` | Update a specific record |
| DELETE | `/records/<id>` | Delete a specific record |

---

## Project Structure

```
rest-api-assignment/
├── app.py                 # Application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── instance/              # Instance-specific files
│   └── database.db        # SQLite database (auto-created)
├── src/
│   ├── __init__.py        # Flask app initialization with Swagger
│   ├── auth.py            # API key authentication decorator
│   ├── models/
│   │   ├── __init__.py
│   │   └── base.py        # Record model definition
│   ├── routes/
│   │   ├── __init__.py
│   │   └── api.py         # API endpoints with Swagger docs
│   └── utils/
│       ├── __init__.py
│       └── helpers.py     # Utility functions
└── tests/
    ├── __init__.py
    └── test_api.py        # Unit tests
```

---

## Production Environment

### Production URL
```
https://rest-api-assignment-five.vercel.app/apidocs/
```

### Production API Endpoint
```
https://rest-api-assignment-five.vercel.app/records
```

### Production Authentication
Use the same API key as local testing:
```
x-api-key: mysecretkey123
```

**Note**: In a production environment, rotate and manage API keys securely using environment variables or secrets management services.

---

## Configuration

### Local Configuration (config.py)
```python
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = "my-secret-api-key"
```

### Environment Variables (For Production)
Set the following environment variables:
- `FLASK_ENV`: `production`
- `API_KEY`: Your secure API key
- `DATABASE_URL`: Your production database URI

---

## API Documentation

### Swagger UI
Access the interactive Swagger UI documentation:
- **Local**: `http://127.0.0.1:5000/apidocs`
- **Production**: `https://rest-api-assignment-five.vercel.app/apidocs/`

The Swagger UI provides:
- Interactive endpoint testing
- Request/response examples
- Parameter documentation
- Authentication configuration

---

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

## Support & Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: "Unauthorized" errors from API
**Solution**: Verify the `x-api-key` header is included in your request:
```bash
-H "x-api-key: mysecretkey123"
```

### Issue: Database not created
**Solution**: The database is automatically created on first run. If needed, delete `instance/database.db` and restart the application.
