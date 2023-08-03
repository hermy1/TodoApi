from fastapi import FastAPI
from os import environ as env


app = FastAPI()

#db connection
# app.py (continued)
DATABASE_URL = "mysql+mysqlconnector://todo:secret@db/todolist"


@app.get('/')
def index():
    return {"hello":f"hi there, were 787 here, {env['APP_NAME']}"}

