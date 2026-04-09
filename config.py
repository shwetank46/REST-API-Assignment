class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Authentication Key
    API_KEY = "my-secret-api-key"