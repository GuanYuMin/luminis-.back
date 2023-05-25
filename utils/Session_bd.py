# Get the database session
from database.database import SessionLocal

# Function to get the database session to use on all routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()