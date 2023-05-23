#!/usr/bin/env python3

"""
An API for the project
"""


from flask_restful import Api, Resource

from auth.users import SignUpResource, Flask, CORS



app = Flask(__name__)
api = Api(app)
CORS(app)



api.add_resource(SignUpResource, "/signup")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
