from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/items/", response_model=schemas.TodoItem)
def create_todo_item(item: schemas.TodoItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_todo_item(db=db, todo_item=item)

@app.get("/items/{item_id}", response_model=schemas.TodoItem)
def read_todo_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = crud.get_todo_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# @app.get("/items/", response_model=list[schemas.TodoItem])
# def read_todo_items(skip: int = 1, limit: int = 10, db: Session = Depends(database.get_db)):
#     items = crud.get_todo_items(db, skip=skip, limit=limit)
#     return items

@app.put("/items/{item_id}", response_model=schemas.TodoItem)
def update_todo_item(item_id: int, item: schemas.TodoItemCreate, db: Session = Depends(database.get_db)):
    db_item = crud.update_todo_item(db, item_id=item_id, todo_item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}", response_model=schemas.TodoItem)
def delete_todo_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = crud.delete_todo_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
