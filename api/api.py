#!/usr/bin/env python3

"""
An API for the project
"""

from bcrypt import gensalt, hashpw
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from MySQLdb import connect, cursors
from os import getenv

from decorators.decorators import validate_user

load_dotenv()

DB_HOST = getenv('DB_HOST')
DB_USER = getenv('DB_USER')
DB_PASSWD = getenv('DB_PASSWD')
DB_NAME = getenv('DB_NAME')

api = Flask(__name__)

CORS(api)

database_object = connect(
    host = DB_HOST,
    user = DB_USER,
    passwd = DB_PASSWD,
    db = DB_NAME
)

cursor = database_object.cursor(cursorclass=cursors.DictCursor)


@api.route("/signup", methods=["POST", "PUT"])
@cross_origin()
@validate_user
def signup():
    """Handle user signup"""
    name = request.form.get("name")
    email = request.form.get('email')
    password = request.form.get('password')
    age = request.form.get("age")
    hashed_pw = hashpw(password.encode('utf-8'), gensalt())
    insert_values = (name, email, age, hashed_pw)

    try:
        cursor.execute("INSERT INTO `app_users` (name, email, age, password) VALUES (%s, %s, %s, %s)", insert_values)
        database_object.commit()
        return jsonify({ "status": "success", "message": f"User {name} created."}), 200
    except Exception as e:
        error_message = str(e.__cause__)
        print(error_message)
        return jsonify({"error": error_message}), 500
    
if __name__ == "__main__":
    api.run(host='0.0.0.0', debug=True)