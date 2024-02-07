import flask
import json
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
    
    def route_boxmodel_css(self):
        return flask.render_template("boxmodel.html")

    def route_biography_css(self):
        if flask.request.method == "GET":
            return flask.render_template('biography.html')
        
        with open('biography.json', 'w') as file:
            form = flask.request.form
            data = form.to_dict()

            json.dump(data, file)
        
        return flask.make_response({'success': True, 'message': 'Stored form data at biography.json!'})
    
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
    APP.add_url_rule('/boxmodel', view_func=routes.route_boxmodel_css)
    
    APP.run(port=9000, debug=False)
