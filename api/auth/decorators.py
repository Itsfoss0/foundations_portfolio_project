#!/usr/bin/env python3

"""
Module with decorators
to used for authentication
and authorization in the application
"""

from flask import request, jsonify, make_response
from functools import wraps
from jwt import decode, DecodeError
from typing import Callable
# from MySQLdb import connect, cursors

from .config import JWT_SECRET_KEY
# from .exceptions import UserAlreadyExists, UserNotAuthorized
from .utils import user_exists


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
            if user_exists(email):
                response = make_response(jsonify({
                    "error": f"user with email {email} exists"
                }))
                response.status_code = 418
                return response

            return function(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)})

    return wrapper


def login_required(function: Callable) -> Callable:
    """
    This is a decorator to ensure that only authorized
    users perform some actions
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        """ The wrapper function"""
        if request.headers.get("Authorization"):
            try:
                tokken = request.headers.get("Authorization").split(" ")[1]
                if tokken:
                    # decode the tokken and retrieve the email
                    decoded_tokken = decode(
                        jwt=tokken,
                        key=JWT_SECRET_KEY,
                        algorithms="HS256"
                    )
                    # return jsonify(decoded_tokken)
                    email = decoded_tokken['email']
                    if user_exists(email):
                        return function(*args, **kwargs)

                    return jsonify({"error": "Session timed out.\
                                   Login and try again"})
            except DecodeError:
                error_mes = make_response(jsonify({"error":
                                          "Login and try again."}))
                error_mes.status_code = 401
                return error_mes
            return jsonify({"error":
                           "Must be logged in to perform this action"})

        return jsonify({"error": "Might wanna login before doing that!"})

    return wrapper
