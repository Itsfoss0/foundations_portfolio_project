#!/usr/bin/env python3

"""
An API for the project
"""

from bcrypt import gensalt, hashpw
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from MySQLdb import connect, cursors
from os import getenv

from decorators.decorators import validate_user

load_dotenv()

DB_HOST = getenv('DB_HOST')
DB_USER = getenv('DB_USER')
DB_PASSWD = getenv('DB_PASSWD')
DB_NAME = getenv('DB_NAME')

app = Flask(__name__)
api = Api(app)
CORS(app)

database_object = connect(
    host=DB_HOST,
    user=DB_USER,
    passwd=DB_PASSWD,
    db=DB_NAME
)
cursor = database_object.cursor(cursorclass=cursors.DictCursor)


class SignUpResource(Resource):
    """
    Class to handle user signup
    """
    @cross_origin()
    @validate_user
    def post(self):
        """Handle user signup"""
        name = request.json.get("name")
        email = request.json.get('email')
        password = request.json.get('password')
        age = request.json.get("age")
        hashed_pw = hashpw(password.encode('utf-8'), gensalt())
        insert_values = (name, email, age, hashed_pw)

        try:
            cursor.execute("INSERT INTO `app_users`\
                            (name, email, age, password) VALUES\
                                (%s, %s, %s, %s)", insert_values)
            database_object.commit()
            return jsonify({"status": "success",
                           "message": f"User {name} created."}), 200
        except Exception as e:
            error_message = str(e.__cause__)
            print(error_message)
            return jsonify({"error": error_message}), 500


api.add_resource(SignUpResource, "/signup")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
