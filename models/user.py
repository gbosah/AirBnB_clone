#!/usr/bin/python3
"""
User class definition
"""
from models.base_model import BaseModel
class User(BaseModel):
    """
    Represents a User
    Attr:
    email(str): Stores the email of the user
    password(str): Stores the password of the user
    first_name(str): Stores the first name of the user
    last_name(str): Stores the last name of the user
    """
    email =""
    password =""
    first_nmae =""
    last_name =""
