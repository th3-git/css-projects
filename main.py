import flask

APP = flask.Flask(__name__)

class Routes:
    def __init__(self) -> None:
        pass

    def route_css(self):
        return flask.render_template("index.html")
    
if __name__ == "__main__":
    routes = Routes()

    APP.add_url_rule('/', view_func=routes.route_css)
    APP.run(port=9000)
