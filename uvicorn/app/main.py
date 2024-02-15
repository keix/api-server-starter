from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas ,models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "api-server-starter!"}


@app.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    if users:
        return users
    else:
        raise HTTPException(status_code=404, detail="404 Page not found.")


@app.get("/users/{user_id}", response_model=schemas.User)
def read_users(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="404 Page not found.")


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

