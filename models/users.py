class Users(db.Model):
    username = db.Column(db.String(50), nullable = False, primary_key = True)
    fk_department = db.Column(db.String(50), db.ForeignKey('department.name'), nullable=True)
    organisations = db.relationship('Organisations', backref='user')
    tasks = db.relationship('Tasks', backref='user')
    tasks = db.relationship('Collabs', backref='user')
