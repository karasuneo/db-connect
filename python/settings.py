import os

from dotenv import load_dotenv

from sqlmodel import create_engine

load_dotenv()

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
db_name = os.getenv("MYSQL_DATABASE")

url: str = f'mysql+mysqlconnector://{user}:{password}@{host}/{db_name}'

engine = create_engine(url, echo=True)

def get_db_engine():
    return engine