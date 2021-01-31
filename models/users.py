class Users(db.Model):
    username = db.Column(db.String(50), nullable = False, primary_key = True)
    isAdmin = db.Column(db.Boolean, default=false)
    fk_department = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=True)
    tasks = db.relationship('Tasks', backref='user')
    tasks = db.relationship('Collabs', backref='user')
