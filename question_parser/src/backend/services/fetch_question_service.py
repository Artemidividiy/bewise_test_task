import requests
from constants.jsservice_api_constants import JS_SERVICE_API_URL
from schemas import QuestionCreate


def fetch_questions(count: int = 1):
    data = requests.get(JS_SERVICE_API_URL + f"?count={str(count)}")
    target: list[QuestionCreate] = [QuestionCreate(
        question=i['question'], answer=i['answer'], created_at=i['created_at']) for i in data.json()]
    return target
