class Collabs(db.Model):
    fk_user = db.Column(db.String(50), db.ForeignKey('users.username'), primary_key = True)
    fk_task = db.Column(db.Integer, db.ForeignKey('tasks.id'), primary_key = True)