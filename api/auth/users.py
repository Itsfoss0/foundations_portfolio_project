#!/usr/bin/env python3

"""
Module with API Resources
to be mapped to User authentication
related API endpoints
"""

from bcrypt import gensalt, hashpw
from flask import jsonify, request
from flask_cors import cross_origin
from flask_restful import Resource
from .decorators import validate_user
from .db.database import cursor_object, db_object


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
            cursor_object.execute("INSERT INTO `app_users`\
                            (name, email, age, password) VALUES\
                                (%s, %s, %s, %s)", insert_values)
            db_object.commit()
            return jsonify({"status": "success",
                           "message": f"User {name} created."}), 200
        except Exception as e:
            error_message = str(e.__cause__)
            # print(error_message)
            return jsonify({"error": error_message}), 500
