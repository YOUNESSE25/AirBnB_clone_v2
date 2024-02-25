#!/usr/bin/python3
"""Instantiates a storage object."""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()

else:
    storage = FileStorage()
storage.reload()
