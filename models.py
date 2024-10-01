from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# User model for police staff
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    badge_number = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Complaint model
class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    register_name = db.Column(db.String(100), nullable=False)
    register_address = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    police_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_reg = db.Column(db.DateTime, default=datetime.utcnow)
    complaint_status = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

# Convict model
class Convict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)
    crime = db.Column(db.String(255), nullable=False)
    police_incharge = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Equipment model
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    date_purchased = db.Column(db.DateTime, nullable=False)
    assigned_policeID = db.Column(db.Integer, db.ForeignKey('user.id'))

# Gun License model
class GunLicense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(100), nullable=False)
    gun = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    bullet_count = db.Column(db.Integer, nullable=False)
