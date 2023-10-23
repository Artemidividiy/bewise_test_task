import models
import schemas
import crud

from fastapi import Depends, FastAPI
from services.fetch_question_service import fetch_questions
from services.db_service import SessionLocal, engine
from sqlalchemy.orm import Session
import models

app = FastAPI()


# @app.middleware("http")
# async def validate_request(request: Request, call_next):
#     pass

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


@app.post("/get_question")
async def get_question(question_num: int, db: Session = Depends(get_db)):
    print(question_num)
    fetched = fetch_questions(count=question_num)
    print(fetched)
    return crud.create_question(db, fetched)
