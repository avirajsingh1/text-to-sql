import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


def execute_sql(sql):
    with engine.connect() as connection:
        result = connection.execute(text(sql))

        rows = result.fetchall()

        return rows