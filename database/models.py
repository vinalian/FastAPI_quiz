import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base = declarative_base()


class Quiz(Base):
    __tablename__ = "quiz"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_text: Mapped[str]
    answer_text: Mapped[str]
    create_date: Mapped[datetime.datetime]

    def __str__(self) -> str:
        return f"id={self.id!r}, Вопрос={self.question_text}"
