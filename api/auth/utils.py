#!/usr/bin/env python3

"""
Module with util functions
should we call them ad-hocks
I have no idea
"""
from jwt import decode, DecodeError
from .db.database import cursor_object, db_object
from .config import JWT_SECRET_KEY
from .exceptions import UserNotAuthorized


def user_exists(email: str) -> bool:
    """
    Check if the user exist in the database
    Args:
        email (str): email of the user to check
    Return:
        True: If the user exists
        False: If the user doesn't exist
    """
    cursor_object.execute("SELECT COUNT(email) FROM `app_users`\
                          WHERE email=%s", (email,))
    result = cursor_object.fetchall()
    exists = int(next(iter(result[0].values())))

    return (exists == 1)


def get_user_id_from_email(email: str) -> int:
    """
    A helper function to retrieve user's
    id given their email
    Args:
        email (str): The email of the user
    Returns:
        The `id` of the user whose email matches `email`
    """
    cursor_object.execute("SELECT `id` from `app_users` WHERE `email`=%s",
                          (email,))
    user_id = cursor_object.fetchall()[0].get('id')
    return user_id


def get_all_user_tasks(user_id: int) -> tuple:
    """
    Gets all the tasks that belong
    to the user, using the user_id as
    the reference point
    Args:
        user_id (int): The ID of the user
    Returns:
        A list of user's tasks (both done and undone)
    """
    cursor_object.execute("SELECT id, title, description,\
        due_date, updated_at, done FROM tasks WHERE created_by=%s",
                          (user_id,))
    tasks_list = cursor_object.fetchall()
    return tasks_list


def decode_user_tokken(tokken: bytes) -> dict:
    """
    Decode a JWT tokken and return it
    Args:
        tokken (str/bytes): The tokken to decode
    Returns:
        dict the tokken's decoded keys and values
    """
    try:
        decoded_tokken = decode(
                    jwt=tokken,
                    key=JWT_SECRET_KEY,
                    algorithms="HS256"
        )
        return decoded_tokken
    except DecodeError:
        raise UserNotAuthorized("User not authorized")


def add_more_tasks(
    user_id: int,
    task_title: str,
    task_description: str,
    done: int
) -> str:
    """
    Create a task and add it in the database
    Args:
        user_id (int): This will be the `created_by` field
        task_title (str): The task's title
        task_description: Task description
        done (int): Task status
    Returns:
        str -> Was the operation sucessful?
    """
    try:
        cursor_object.execute(
            "INSERT INTO tasks (created_by, title, description, done)\
            VALUES (%s, %s, %s, %s)",
            (user_id, task_title, task_description, done)
        )
        db_object.commit()
        return f"New task {task_title} created."
    except Exception as e:
        return f"could not add {task_title}, {str(e)}"
