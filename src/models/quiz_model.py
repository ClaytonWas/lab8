# src/models/quiz_model.py
from src.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, PickleType


class QuizModel(db.Model):
    __tablename__ = 'quizzes'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    questions: Mapped[list] = mapped_column(PickleType)

    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_quiz(cls, quiz_id):
        return cls.query.get(quiz_id)
