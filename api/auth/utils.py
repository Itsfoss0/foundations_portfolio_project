#!/usr/bin/env python3

"""
Module with util functions
should we call them ad-hocks
I have no idea
"""

from .db.database import cursor_object, DB_NAME


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
    cursor_object.execute("SELECT title, description, due_date, done FROM   `tasks` WHERE `created_by`=%s",
                          (user_id,))
    tasks_list = cursor_object.fetchall()
    return tasks_list
