import flask

APP = flask.Flask(__name__)

class Routes:
    def __init__(self) -> None:
        self.user_db = [
            {'username': "alzar", 'password': 'python'}
        ]

    def route_css(self):
        return flask.render_template("index.html")
    
    def route_inline_css(self):
        return flask.render_template("inlinestylesheet.html")
    
    def auth_endpoint(self):
        body = flask.request.form
        username = body.get('username')
        password = body.get("password")

        if self.user_db[0].get("username") != username:
            return flask.make_response("INVALID_USER", 400)
        
        if self.user_db[0].get("password") != password:
            return flask.make_response("INVALID_PASSWORD", 400)
        
        return flask.make_response("AUTHORIZED", 200)
    
if __name__ == "__main__":
    routes = Routes()

    APP.add_url_rule('/', view_func=routes.route_css)
    APP.add_url_rule('/authenticate', view_func=routes.auth_endpoint, methods=['POST'])
    APP.add_url_rule('/inline-css', view_func=routes.route_inline_css)

    APP.run(port=9000, debug=True)
