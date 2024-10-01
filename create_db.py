from app import app, db

# Create all the tables defined in models.py
with app.app_context():
    db.create_all()

print("Database created successfully!")
