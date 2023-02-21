#!/usr/bin/python3
'''contains the city class'''
from models.base_model import BaseModel


class City(BaseModel):
    '''The city class'''
    state_id = ""  # it will be the `State.id`
    name = ""
