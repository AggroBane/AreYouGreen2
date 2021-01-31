class Owner(db.Model):
    username = db.Column(db.String(50), nullable = False, primary_key = True)
    organisations = db.relationship('Organisations', backref='owner')
