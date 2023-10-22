from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from services.db_service import Base


class Question(Base):
    __tablename__ = "questions"
    id = Column("id", Integer, primary_key=True, index=True)
    question_text = Column("question_text", String,
                           nullable=False, unique=True)
    answer_text = Column("answer_text", String, nullable=False, unique=True)
    question_created_at = Column(
        "question_created_at", DateTime, nullable=False, unique=True)
