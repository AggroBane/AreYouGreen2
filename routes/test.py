from . import routes

@routes.route("/test")
def test():
    return "This is test!"
