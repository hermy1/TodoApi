from fastapi import FastAPI
from os import environ as env


app = FastAPI()

#db connection
DATABASE_URL = "mysql+mysqlconnector://username:password@db/db_name"


@app.get('/')
def index():
    return {"hello":f"hi there, were 787 here, {env['APP_NAME']}"}

