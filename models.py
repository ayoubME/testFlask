# models.py
# Creator: Max Greenwald
# Updated: 3/20/17
# Purpose: Define models and relevant functions for the database with SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    # Gets dict with the Doctor object and all of its associated reviews
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'status': [self.status]
        }
