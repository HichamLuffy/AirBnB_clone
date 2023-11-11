#!/usr/bin/python3
"""Base Model
Usage:
python3 models/base_model.py
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel"""
    def __init__(self, *args, **kwargs):
        """init"""
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            del kwargs['__class__']
            for key, val in kwargs.items():
                if key != "__class__":
                    setattr(self, key, val)
            self.created_at = datetime.strptime(self.created_at, timeformat)
            self.updated_at = datetime.strptime(self.updated_at, timeformat)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        storage.new(self)

    def save(self):
        """save"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to_dict"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                new_dict[key] = val.isoformat()
            else:
                new_dict[key] = val
        return new_dict

    def __str__(self):
        """__str__"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
