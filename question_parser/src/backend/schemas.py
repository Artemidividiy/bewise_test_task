from pydantic import BaseModel
import models


class QuestionBase(BaseModel):
    question: str
    answer: str
    created_at: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int
    created_at: int
    updated_at: int

    class Config:
        orm_mode = True

    class Meta:
        orm_model = models.Question
