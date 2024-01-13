#!/usr/bin/python3
"""The `review` module.

It defines one class, `Review(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review

    Attributes:, text,user_id,place_id
    """

    text = ""
    user_id = ""
    place_id = ""
