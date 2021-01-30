class User(Document):
    name = StringField(required=True, max_length=200)
    content = StringField(required=True)