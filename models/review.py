#!/usr/bin/python3
"""
Defines the Review class
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Attr:
    place_id(str): Stores The Place id.
    user_id(str): Stores The User id.
    text(str): Stores The text of The Review
    """
    place_id = ""
    user_id =""
    text = ""
