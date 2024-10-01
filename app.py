from flask import Flask, request, jsonify
from models import db, User, Complaint, Convict, Equipment, GunLicense
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///police_records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(name=data['name'], badge_number=data['badge_number'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(badge_number=data['badge_number']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"message": "Invalid credentials!"}), 401
    return jsonify({"message": "Login successful!"})

@app.route('/complaint', methods=['POST'])
def create_complaint():
    data = request.get_json()
    new_complaint = Complaint(
        register_name=data['register_name'],
        register_address=data['register_address'],
        description=data['description'],
        police_id=data['police_id'],
        complaint_status=data['complaint_status'],
        phone=data['phone']
    )
    db.session.add(new_complaint)
    db.session.commit()
    return jsonify({"message": "Complaint created successfully!"})

@app.route('/convict', methods=['POST'])
def create_convict():
    data = request.get_json()
    new_convict = Convict(
        name=data['name'],
        age=data['age'],
        height=data['height'],
        crime=data['crime'],
        police_incharge=data['police_incharge']
    )
    db.session.add(new_convict)
    db.session.commit()
    return jsonify({"message": "Convict added successfully!"})

@app.route('/equipment', methods=['POST'])
def add_equipment():
    data = request.get_json()
    new_equipment = Equipment(
        item_name=data['item_name'],
        date_purchased=data['date_purchased'],
        assigned_policeID=data['assigned_policeID']
    )
    db.session.add(new_equipment)
    db.session.commit()
    return jsonify({"message": "Equipment added successfully!"})

@app.route('/gunlicense', methods=['POST'])
def add_gun_license():
    data = request.get_json()
    new_gun_license = GunLicense(
        owner_name=data['owner_name'],
        gun=data['gun'],
        address=data['address'],
        phone=data['phone'],
        expiry_date=data['expiry_date'],
        bullet_count=data['bullet_count']
    )
    db.session.add(new_gun_license)
    db.session.commit()
    return jsonify({"message": "Gun License added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
