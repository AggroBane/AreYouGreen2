from app import db
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(128), nullable = True)
    checked = db.Column(db.Boolean, default=False)
    score = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime)
    date_completed = db.Column(db.DateTime)
    fk_assignedUser = db.Column(db.String(50), db.ForeignKey('users.username'))
    fk_department = db.Column(db.Integer, db.ForeignKey('departments.id'))
    collaborators = db.relationship('Collabs', backref='task')

