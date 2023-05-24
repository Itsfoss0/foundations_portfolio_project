#!/usr/bin/env python3

"""
Module with API Resources
to be mapped to User authentication
related API endpoints
"""

from bcrypt import gensalt, hashpw, checkpw
from flask import jsonify, request, make_response
from flask_cors import cross_origin
from flask_restful import Resource
from jwt import encode
from .decorators import validate_user
from .db.database import cursor_object, db_object
from .config import JWT_SECRET_KEY


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
            error_message = str(e)
            return jsonify({"error": error_message}), 500


class LoginResource(Resource):
    """
    Class to handle user login functionalities
    """
    def post(self):
        """
        Send a POST request with the email
        and password to login. If the credentials match
        those stored in the database, return a JWT token
        to the client. If not, raise an InvalidCredentials
        exception (or send a 401 response)
        """
        try:
            if request.json.get('email') and request.json.get('password'):
                email = request.json.get('email')
                password = request.json.get('password')

                cursor_object.execute("SELECT `password` FROM\
                                      `app_users` WHERE email= %s", (email,))
                stored_pw = cursor_object.fetchone()
                if stored_pw is not None:
                    if checkpw(password.encode("utf-8"),
                               stored_pw['password'].encode('utf-8')):
                        payload = {
                            "email": email,
                            "is_admin": "false"
                        }
                        tokken = encode(
                            payload=payload,
                            key=JWT_SECRET_KEY,
                            algorithm="HS256")
                        return jsonify({"user": email, "tokken": tokken})

                invalid_creds_resp = make_response(jsonify({"error":
                                                   "Invalid credentials"}))
                invalid_creds_resp.status_code = 401
                return invalid_creds_resp

            no_email_pwd = make_response(jsonify({"error":
                                         "Need an email and password"}))
            no_email_pwd.status_code = 401
            return no_email_pwd

        except Exception as e:
            exception_raised_resp = make_response(jsonify({"error": str(e)}))
            exception_raised_resp.status_code = 500
            return exception_raised_resp
