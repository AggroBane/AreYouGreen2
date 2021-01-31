class Collabs(db.Model):
    fk_user = db.Column(db.String(50), db.ForeignKey('user.username'), primary_key = True)
    fk_task = db.Column(db.Integer, db.ForeignKey('task.id'), primary_key = True)