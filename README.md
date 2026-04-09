# rest-api-assignment

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/rest-api-assignment.git
   cd rest-api-assignment
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application locally, execute the following command:
```
python app.py
```

The application will start on `http://127.0.0.1:5000`.

## API Documentation

The API documentation is available via Swagger at the following URL:
```
http://127.0.0.1:5000/apidocs
```

## API Authentication

Please ensure to include the API key in the headers for authentication when making requests to the API.

## Project Structure

- `app.py`: Entry point of the application.
- `config.py`: Configuration settings for the application.
- `src/`: Contains the application logic, including models, routes, and utilities.
- `tests/`: Contains unit tests for the application.

## License

This project is licensed under the MIT License.