#!/usr/bin/env python3

"""database and cursor objects module"""

from dotenv import load_dotenv
from MySQLdb import connect, cursors
from os import getenv

load_dotenv()

DB_HOST = getenv('DB_HOST')
DB_USER = getenv('DB_USER')
DB_PASSWD = getenv('DB_PASSWD')
DB_NAME = getenv('DB_NAME')


db_object = connect(
    host=DB_HOST,
    user=DB_USER,
    passwd=DB_PASSWD,
    db=DB_NAME
)
cursor_object = db_object.cursor(cursorclass=cursors.DictCursor)
