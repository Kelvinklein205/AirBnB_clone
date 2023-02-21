#!/usr/bin/python3
"""The base class for the airbnb project
This file contains the BaseModel class for the project
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    '''The BaseModel class that defines all common
    attributes/methods for other classes
    Attributes:
        id (str): string - assign with an uuid when an instance is created
            the goal is to have unique id for each BaseModel
        created_at: datetime - assign with the current datetime when
            an instance is created
        updated_at: datetime - assign with the current datetime when
            an instance is created and it will be updated every time
            you change your object
        **kwargs (obj: `dict`, optional): a dict with attributes from
            another obj of the same class can be provided to recreate the class
    '''

    def __init__(self, *args, **kwargs):
        '''The init method for the class'''

        if len(kwargs) > 3:
            self.id = kwargs['id']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''The string representation for the object when it is printed'''
        string = "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)
        return string

    def save(self):
        '''saves the model to a file (database) and update the
        `updated_at attribute`
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Creates a dictionary of all the attributes in the object
        Returns the dictionary
        '''
        my_dict = {}
        for key, value in self.__dict__.items():
            my_dict[key] = value
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict
