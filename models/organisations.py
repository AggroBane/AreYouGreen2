class Organisations(db.Model):
    name = db.Column(db.String(50), nullable = False, primary_key=True)
    fk_owner = db.Column(db.String(50), db.ForeignKey('users.username'))
    departments = db.relationship('Departments', backref='organisation')
