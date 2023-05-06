from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem

templates = Jinja2Templates(directory="templates/")

todo_routes = APIRouter()

todo_list = []


@todo_routes.get("/todo/{todo_id}")
# get todo element
async def get_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": f"Element with ID {todo_id} doesnt exist"}


@todo_routes.get("/todo")
async def retrieve_todos(request: Request):
    return templates.TemplateResponse("todos.html", {
        "request": request,
        "todos": todo_list
    })


@todo_routes.post("/todo")
# add todo element
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todos.html", {
        "request": request,
        "todos": todo_list
    })


@todo_routes.post("/todo")
# delete all elements
async def delete_all_todos(request: Request, todo: Todo = None):
    if not todo_list:
        return {"message": "Todo list is empty"}
    else:
        todo_list.clear()
        return templates.TemplateResponse("todos.html", {
            "request": request,
            "todos": todo_list
        })
    
# @todo_routes.delete("/todo")
# # delete all elements
# async def delete_all_todos(request: Request):
#     if not todo_list:
#         return {"message": "Todo list is empty"}
#     else:
#         todo_list.clear()
#         return templates.TemplateResponse("todos.html", {
#             "request": request,
#             "todos": todo_list
#         })

