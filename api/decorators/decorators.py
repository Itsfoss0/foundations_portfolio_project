#!/usr/bin/env python3

"""
Module with custom decoratorsto be ensure smooth signup
"""

from flask import request
from functools import wraps
from typing import Callable


class UserAlreadyExists(Exception):
    """
    Their already exists a user with the
    specified username/email combination
    """

    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(message)


class UserNotAuthorized(Exception):
    """
    The user is not authorized to perfom
    the action we are trying to do
    """

    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(message, code)


def validate_user(cursor: object) -> Callable:

    def validate_user_decorator(function: Callable) -> Callable:
        """
        Validate User decorator:
        This decorator can be applied to the signup
        to ensure that no duplicate users are created
        in the database.
        Args:
            function (Callable): A function to be applied to
        Returns:
            returns a callable (function object)
        """

        email = request.form.get('email')

        @wraps(function)
        def wrapper(*args: list, **kwargs: dict) -> Callable:
            """The wrapper function"""
            cursor.execute('SELECT COUNT (*) FROM `app_users` WHERE email=%s',
                           (email))
            cursor_res = cursor.fetchall()
            existing_users = int(next(iter(cursor_res[0].values())))

            if existing_users < 1:
                return function(*args, **kwargs)
            else:
                raise UserAlreadyExists(f"A user with email {email}\
                                        already exists")

        return wrapper

    return validate_user_decorator
