from sqlalchemy.engine import create
import models
import schemas
from sqlalchemy.orm import Session


def create_question(db: Session, questions: list[schemas.QuestionCreate]):
    """Метод Question.create"""
    target = []
    for question in questions:
        db_question = models.Question(
            question_text=question.question,
            answer_text=question.answer,
            question_created_at=question.created_at,
            question_id=question.id,
            created_at=question.created_at,
            updated_at=question.updated_at)
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        target.append(db_question)
    return target


def get_questions(db: Session):
    """Метод Question.read"""
    return db.query(models.Question).all()
