class Departments(db.Model):
    name = db.Column(db.String(50), nullable = False, primary_key = True)
    fk_orgName = db.Column(db.String(50), db.ForeignKey('organisations.name'))
    users = db.relationship('Users', backref='department')
