from fastapi import FastAPI, Request
from services.fetch_question_service import fetch_questions
app = FastAPI()


# @app.middleware("http")
# async def validate_request(request: Request, call_next):
#     pass


@app.post("/get_question")
async def get_question(question_num: int):
    print(question_num)
    return fetch_questions(count=question_num)

