from fastapi import FastAPI
from pydantic import BaseModel
from database.functions import *
from app.misc import *

import datetime

app = FastAPI()


class QuizSchema(BaseModel):
    id: int
    question_text: str
    answer_text: str
    create_date: datetime.datetime


@app.post("/{count}")
async def get_biggest_cities(count: int):
    last_question = await get_last_question()

    valide_count = await validate_count(count)
    if valide_count is False:
        return {'status': 'Error! Count must be a positive integer'}

    quiz = await get_quiz(count=valide_count)

    if quiz is None:
        return {'status': 'Error! Have no quiz!'}

    await save_new_question(quiz)

    if last_question is None:
        return last_question

    return {'id': last_question.id,
            'question_text': last_question.question_text,
            'answer_text': last_question.answer_text,
            'create_date': last_question.create_date
            }
