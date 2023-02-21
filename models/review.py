#!/usr/bin/python3
'''contains the review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''The review class'''
    place_id = ""  # it will be the `Place.id`
    user_id = ""  # it will be the `User.id`
    text = ""
