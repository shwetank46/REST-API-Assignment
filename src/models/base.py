from src import db

class Record(db.Model):
    __tablename__ = "records"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "status": self.status
        }