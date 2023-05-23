from flask import request, jsonify
from functools import wraps
from typing import Callable
from MySQLdb import connect, cursors

from .exceptions import UserAlreadyExists, UserNotAuthorized


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

        database_object = connect(
            host="localhost",
            user="todoist_user_dev",
            passwd="user_1_dev",
            db="todoist_db"
        )

        cursor = database_object.cursor(cursorclass=cursors.DictCursor)

        try:
            cursor.execute('SELECT COUNT(*) FROM `app_users` WHERE\
                           email=%s', (email,))
            cursor_res = cursor.fetchall()
            existing_users = int(next(iter(cursor_res[0].values())))

            cursor.close()
            database_object.close()

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
