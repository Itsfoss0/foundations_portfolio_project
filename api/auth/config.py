#!/usr/bin/env python3

"""
This module holds the secret keys
to be used in the application, including
JWT secret keys, database names and passwords
and third party API keys
"""

from dotenv import load_dotenv
from os import getenv

load_dotenv()

JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
