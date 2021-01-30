from . import routes

@routes.route('/')
def index():
    return 'This is index!'

