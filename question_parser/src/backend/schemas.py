from pydantic import BaseModel
from datetime import datetime
import models


class QuestionBase(BaseModel):
    question: str
    answer: str
    created_at: str


class QuestionCreate(QuestionBase):
    id: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True

    class Meta:
        orm_model = models.Question
