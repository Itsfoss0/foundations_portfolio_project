#!/usr/bin/env python3

"""
Module with the tasks resources
These will be mapped to the /task
endpoint, to create, edit, delete
and get tasks
"""


from flask import request, jsonify, make_response
from flask_cors import cross_origin
from flask_restful import Resource

from .decorators import login_required
from .exceptions import UserNotAuthorized
from .utils import get_all_user_tasks, get_user_id_from_email,\
    add_more_tasks, decode_user_tokken, delete_task


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
            decoded_tokken = decode_user_tokken(user_token)
            user_email = decoded_tokken["email"]
            user_id = get_user_id_from_email(user_email)
            tasks = get_all_user_tasks(user_id)
            return jsonify({"user": user_id, "email":
                            user_email, "tasks": tasks})
        except (UserNotAuthorized):
            return jsonify({"error": "user not athorized"})

    @cross_origin()
    @login_required
    def post(self):
        """
        Creating a new task and adding it
        to the database
        """
        try:
            user_token = request.headers.get("Authorization").split(" ")[1]
            decoded_tokken = decode_user_tokken(user_token)
            user_email = decoded_tokken["email"]
            # the user_id correspond to the task owner
            user_id = get_user_id_from_email(user_email)
            task_title = request.json.get("title")
            task_description = request.json.get("description")
            task_status = request.json.get("done")
            result = add_more_tasks(
                user_id=user_id,
                task_title=task_title,
                task_description=task_description,
                done=task_status
            )
            return jsonify({
                "status": "success",
                "message": f"{result}"
                })
        except Exception as e:
            error_resp = make_response(jsonify({
                "error": "Uknown error occured",
                "message": str(e),
                "status": "failed"
            }))
            error_resp.status_code = 500
            return error_resp

    @login_required
    @cross_origin()
    def delete(self):
        """
        Delete a task from the database
        For whatever reason
        """
        if request.json.get("task_id") is not None:
            try:
                task_id = request.json.get("task_id")
                user_tokken = request.headers.get("Authorization").split(" ")[1]
                decoded_tokken = decode_user_tokken(user_tokken)
                user_email = decoded_tokken['email']
                user_id = get_user_id_from_email(user_email)
                task_deleted_message = delete_task(task_id, user_id)
                return jsonify({
                    "status": "success",
                    "message": task_deleted_message
                })
            except Exception as e:
                error_resp = make_response(jsonify({"error": str(e)}))
                error_resp.status_code = 500
                return (error_resp)

        error_resp = make_response(jsonify({
            "error": "Bad Request",
            "message": "Which task to delete?"
        }))
        error_resp.status_code = 400
        return error_resp
