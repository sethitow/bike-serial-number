import logging

from flask import Flask
from flask_graphql import GraphQLView

import flask_login

from schema import schema

app = Flask(__name__)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

logging.basicConfig(level=logging.DEBUG)

@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get("Authorization")
    if api_key == "Bearer faketoken":
        return flask_login.UserMixin()
    else:
        return flask_login.AnonymousUserMixin()

@app.route("/graphql", methods=["POST", "GET"])
@flask_login.login_required
def graphql_func(*args, **kwargs):
    return GraphQLView.as_view("graphql", schema=schema, graphiql=True)(*args, **kwargs)


if __name__ == "__main__":
    app.run(debug=True)
