#!/usr/bin/env python3

"""
An API for the project
"""

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from auth.users import SignUpResource, LoginResource
from auth.tasks import TaskResource

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(SignUpResource, "/signup")
api.add_resource(LoginResource, "/login")
api.add_resource(TaskResource, "/tasks")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
