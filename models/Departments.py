from app import db
class Departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    fk_orgName = db.Column(db.String(50), db.ForeignKey('organisations.name'))
    users = db.relationship('Users', backref='department')
