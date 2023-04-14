from fastapi import APIRouter
from model import Todo, TodoItem

todo_routes = APIRouter()

todo_list = []

# @todo_routes.get("/todo")
# async def get_all_todos()-> dict:


@todo_routes.get("/todo/{todo_id}")
# get todo element
async def get_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": f"Element with ID {todo_id} doesnt exist"}


@todo_routes.post("/todo")
# add todo element
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added correctly"}


@todo_routes.put("/todo/{todo_id}")
# update todo element
async def update_todo(todo_id: int, item: TodoItem) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = item.item
            return {"message": f"Element {todo_id} updated correctly"}
    return {"message": f"Element with ID {todo_id} doesnt exist"}
