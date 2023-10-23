import models
import schemas
from sqlalchemy.orm import Session


def create_question(db: Session, questions: list[schemas.QuestionCreate]):
    print(questions)
    target = []
    for question in questions:
        db_question = models.Question(question_text=question.question,
                                      answer_text=question.answer, question_created_at=question.created_at)
        print(db_question.__str__())
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        target.append(db_question)
    return target
