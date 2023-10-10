import datetime

from database.connector import get_session
from sqlalchemy import select, insert
from database.models import Quiz
from typing import List, Dict

__all__ = [
    'get_last_question',
    'save_new_question'
]


async def get_last_question() -> Quiz:
    session = await get_session()
    result = await session.execute(select(Quiz).order_by(Quiz.create_date.desc()).limit(1))
    return result.scalars().one_or_none()


async def save_new_question(questions: List[Dict]) -> bool:
    session = await get_session()
    for question in questions:
        await session.execute(
            insert(Quiz).values(
                id=question['id'],
                question_text=question['question'],
                answer_text=question['answer'],
                create_date=datetime.datetime.strptime(
                    question['created_at'].replace('Z', ''),
                    '%Y-%m-%dT%H:%M:%S.%f')
            ))
        await session.commit()
