#!/usr/bin/env python3
class UserAlreadyExists(Exception):
    """
    There already exists a user with the
    specified username/email combination
    """

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class UserNotAuthorized(Exception):
    """
    The user is not authorized to perform
    the action we are trying to do
    """

    def __init__(self, message):
        self.message = message
        super().__init__(message)