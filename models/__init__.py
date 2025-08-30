#!/usr/bin/python3
""" Initialize the models package """

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

dummy_tables = {
   "users": User,
   "states": State,
   "cities": City,
   "amenities": Amenity,
   "places": Place,
   "reviews": Review
}

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
