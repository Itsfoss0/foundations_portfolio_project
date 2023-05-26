#!/usr/bin/env python3

"""
Module with the tasks resources
These will be mapped to the /task
endpoint, to create, edit, delete
and get tasks
"""


from flask import request, jsonify
from flask_cors import cross_origin
from flask_restful import Resource
from jwt import decode, DecodeError

from .decorators import login_required
from .db.database import db_object, cursor_object
from .config import JWT_SECRET_KEY
from .exceptions import UserNotAuthorized
from .utils import get_all_user_tasks, get_user_id_from_email

class TaskResource(Resource):
    """
    The tasks resource class
    Methods:
        get() -> Retrieve users' tasks
        post() -> Add a task
        put() -> Modify a task's props
        delete() -> Delete a task
    """
    @cross_origin()
    @login_required
    def get(self):
        try:
            """When sending a GET request"""
            user_token = request.headers.get("Authorization").split(" ")[1]
            decoded_tokken = decode(
                jwt=user_token,
                key=JWT_SECRET_KEY,
                algorithms="HS256"
            )
            user_email = decoded_tokken["email"]
            user_id = get_user_id_from_email(user_email)
            tasks = get_all_user_tasks(user_id)
            return jsonify({"user": user_id, "email": user_email, "tasks": tasks})
        except (UserNotAuthorized, DecodeError):
            return jsonify({"error": "user not athorized"})
