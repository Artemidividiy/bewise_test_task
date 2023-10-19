import requests
from constants.jsservice_api_constants import JS_SERVICE_API_URL


def fetch_questions(count: int = 1):
    data = requests.get(JS_SERVICE_API_URL + f"?count={str(count)}")
    print(data.json())
    return data.json()

