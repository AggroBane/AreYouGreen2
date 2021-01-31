from app import db
class Organisations(db.Model):
    name = db.Column(db.String(50), nullable = False, primary_key=True)
    departments = db.relationship('Departments', backref='organisation')
