from sqlalchemy.orm import Session
from . import models, schemas

def get_todo_item(db: Session, item_id: int):
    return db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()

# def get_todo_items(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.TodoItem).offset(skip).limit(limit).all()

def create_todo_item(db: Session, todo_item: schemas.TodoItemCreate):
    db_item = models.TodoItem(**todo_item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_todo_item(db: Session, item_id: int, todo_item: schemas.TodoItemCreate):
    db_item = get_todo_item(db, item_id)
    if db_item:
        for key, value in todo_item.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    return None

def delete_todo_item(db: Session, item_id: int):
    db_item = get_todo_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
        return db_item
    return None
