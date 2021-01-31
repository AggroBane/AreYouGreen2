class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(128), nullable = True)
    checked = db.Column(db.Boolean, default=False)
    fk_assignedUser = db.Column(db.String(50), db.ForeignKey('user.username'))
    fk_department = db.Column(db.String(50), db.ForeignKey('department.name'))
    collaborators = db.relationship('Collabs', backref='task')

