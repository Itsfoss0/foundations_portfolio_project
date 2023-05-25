#!/usr/bin/env python3

"""
Module with decorators
to used for authentication
and authorization in the application
"""

from flask import request, jsonify, make_response
from functools import wraps
from jwt import decode
from typing import Callable
# from MySQLdb import connect, cursors

from .exceptions import UserAlreadyExists, UserNotAuthorized
from .config import JWT_SECRET_KEY
from .db.database import cursor_object


def validate_user(function: Callable) -> Callable:
    """
    Validate User decorator:
    This decorator can be applied to the signup
    to ensure that no duplicate users are created
    in the database.
    Args:
        function (Callable): A function to be applied to function object
    Returns:
        returns a callable (function object)
    """
    @wraps(function)
    def wrapper(*args: list, **kwargs: dict) -> Callable:
        """The wrapper function"""
        email = request.json.get("email")

        try:
            cursor_object.execute('SELECT COUNT(*) FROM `app_users` WHERE\
                           email=%s', (email,))
            cursor_res = cursor_object.fetchall()
            existing_users = int(next(iter(cursor_res[0].values())))

            # cursor_object.close()
            # db_object.close()

            if existing_users < 1:
                return function(*args, **kwargs)
            else:
                error_message = f"A user with email {email} already exists"
                return jsonify({"error": error_message,
                               "status": "error"}), 400

        except UserAlreadyExists as e:
            error_message = str(e)
            return jsonify({"error": error_message}), 400

    return wrapper


def login_required(function: Callable) -> Callable:
    """
    This is a decorator to ensure that only authorized
    users perform some actions
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        """ The wrapper function"""
        tokken = request.headers.get("Authorization")
        if tokken:
            try:
                # get the tokken from the tokken header
                # Authorization: Basic eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.djs
                tokken = tokken.split(" ")[1]
                decoded_tok = decode(
                    jwt=tokken,
                    key=JWT_SECRET_KEY,
                    algorithms="HS256")
                user_email = decoded_tok.get("email")
                cursor_object.execute("SELECT COUNT(*) FROM `app_users` \
                                      WHERE `email` = %s", (user_email))
                cursor_res = cursor_object.fetchone()
                # is there a user in the database with the email?
                email_found = int(next(iter(cursor_res[0].values())))
                if email_found == 1:
                    return function(*args, **kwargs)

            except Exception:
                raise UserNotAuthorized("User not authorized")

        erro_mess = make_response(jsonify({"error": "You are not\
                                  authorized to perfom this action"}))
        erro_mess.status_code = 401
        return erro_mess

    return wrapper
