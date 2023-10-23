from itertools import count
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from rich.console import Console
from rich.table import Table
import crud
import models
import schemas
from services.db_service import SessionLocal, engine
from services.fetch_question_service import fetch_questions

app = FastAPI()
console = Console()

# @app.middleware("http")
# async def validate_request(request: Request, call_next):
#     pass

models.Base.metadata.create_all(bind=engine)

def render_table(data: list):
    """отображает таблицу с теми вопросами, которые не были добавлены в бд по причине их наличия"""
    if len(data) == 0: 
        return
    console.print("This values were already in db")
    table = Table()
    table.add_column("id")
    table.add_column("text")
    table.add_column("answer")
    for i in data:
        table.add_row(str(i.id), i.question, i.answer)
    console.print(table)


def find(models_arr: list[models.Question], schema_item: schemas.QuestionCreate):
    """Метод для поиска добавляемого вопроса среди уже существующих в бд"""
    for i in range(len(models_arr)):
        if models_arr[i].question_id == schema_item.id:
            print(models_arr[i].question_id)
            return i
    return -1


def get_db():
    """Метод для получения сессии бд"""
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


@app.post("/get_question")
async def get_question(question_num: int, db: Session = Depends(get_db)):
    fetched = fetch_questions(count=question_num)
    in_db = crud.get_questions(db=db)
    already_in_db: list[schemas.QuestionCreate] = []
    while len(fetched):
        if (find(in_db, fetched[0]) == -1):
            crud.create_question(db, [fetched[0]])
            fetched.pop(0)
        else:
            already_in_db.append(fetched[0])
            fetched[0] = fetch_questions(count=1)[0]
    render_table(already_in_db)
    return crud.get_questions(db=db)[-1]
