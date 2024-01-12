import json
import flask

APP = flask.Flask(__name__)

class Routes:
    def __init__(self) -> None:
        self.user_db = [
            {'username': "alzar", 'password': 'python'}
        ]

    def route_css(self):
        return flask.render_template("index.html")
    
    def auth_endpoint(self):
        json_data = flask.request.json
        username = json_data.get('username')
        password = json_data.get('password')

        db_entry_alzar = self.user_db[0]
        if username == db_entry_alzar['username'] and password == db_entry_alzar['password']:
            return flask.jsonify("User authorized, hello 'alzar'!")
        
        return flask.jsonify("Sorry, not authorized.")
    
if __name__ == "__main__":
    routes = Routes()

    APP.add_url_rule('/', view_func=routes.route_css)
    APP.add_url_rule('/authenticate', view_func=routes.auth_endpoint, methods=['POST'])
    APP.run(port=9000)
