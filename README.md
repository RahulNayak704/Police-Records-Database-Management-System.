# Police Records Management System

## Description
This project is a Police Records Management System that allows police staff to register, log in, and manage complaints, convicts, equipment, and gun licenses in a police station. It uses Flask as the web framework and SQLAlchemy for database operations.

## Installation
1. Clone the repository:
2. Navigate into the project directory: `cd police-records-management`.
3. Install the required dependencies: `pip install -r requirements.txt`.
4. Create the database: `python create_db.py`.
5. Run the Flask application: `python app.py`.

The application will be running on http://127.0.0.1:5000/


Usage

1. Register a New User (Police Staff)
To register a new police officer, make a POST request to /register with the following JSON structure:

POST /register
Content-Type: application/json
{
  "name": "John Doe",
  "badge_number": "12345",
  "password": "your_password"
}

2. Log In as a User
To log in as a police officer, make a POST request to /login with the following JSON structure:

POST /login
Content-Type: application/json
{
  "badge_number": "12345",
  "password": "your_password"
}

3. Create a Complaint
To create a new complaint, make a POST request to /complaint with the following JSON structure:

POST /complaint
Content-Type: application/json
{
  "register_name": "Jane Doe",
  "register_address": "123 Street, City",
  "description": "Description of the complaint",
  "police_id": 1,
  "complaint_status": "Open",
  "phone": "1234567890"
}

4. Add a Convict
To add a new convict, make a POST request to /convict with the following JSON structure:

POST /convict
Content-Type: application/json
{
  "name": "Mike Johnson",
  "age": 35,
  "height": 6.1,
  "crime": "Robbery",
  "police_incharge": 1
}

5. Add Equipment
To add new equipment, make a POST request to /equipment with the following JSON structure:

POST /equipment
Content-Type: application/json
{
  "item_name": "Handcuffs",
  "date_purchased": "2024-01-01",
  "assigned_policeID": 1
}

6. Add a Gun License
To add a new gun license, make a POST request to /gunlicense with the following JSON structure:

POST /gunlicense
Content-Type: application/json
{
  "owner_name": "Jack Sparrow",
  "gun": "Pistol",
  "address": "456 Harbor Rd, City",
  "phone": "9876543210",
  "expiry_date": "2025-12-31",
  "bullet_count": 50
}
