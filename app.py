from fastapi import FastAPI
from todos import todo_routes

app = FastAPI()

app.include_router(todo_routes)


