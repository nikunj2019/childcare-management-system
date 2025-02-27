from sqlalchemy.orm import Session
from models.child import Child
from database import get_db

def get_children():
    db: Session = get_db()
    return db.query(Child).all()

def add_child(child_data):
    db: Session = get_db()
    child = Child(**child_data)
    db.add(child)
    db.commit()
    return True