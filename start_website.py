import os
from database.connector import init_models
import asyncio
from os import environ
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    asyncio.run(init_models())
    os.system(f'uvicorn main:app --reload --port 8010')
