# User ORM for SQLAlchemy 
class User(db.Model): 
    username = db.Column(db.String(50), nullable = False, primary_key = True)