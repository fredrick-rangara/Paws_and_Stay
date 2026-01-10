from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)

    # Relationship 1: One-to-Many (Owner to Pets)
    pets = db.relationship('Pet', backref='owner', lazy=True)
    # Relationship 2: Many-to-Many through StaySession
    stay_sessions = db.relationship('StaySession', backref='sitter', lazy=True)

class Pet(db.Model, SerializerMixin):
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String)
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # One-to-Many (Pet to StaySessions)
    sessions = db.relationship('StaySession', backref='pet', lazy=True)

class StaySession(db.Model, SerializerMixin):
    __tablename__ = 'stay_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    sitter_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # REQUIRED: User submittable attributes
    special_instructions = db.Column(db.String)
    daily_rate = db.Column(db.Float)