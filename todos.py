from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem

templates = Jinja2Templates(directory="templates/")

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


@todo_routes.get("/todo")
async def retrieve_todos(request: Request):
    return templates.TemplateResponse("todos.html", {
        "request": request,
        "todos": todo_list
    })


@todo_routes.post("/todo")
# add todo element
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo_list.append(todo)
    return templates.TemplateResponse("todos.html", {
        "request": request,
        "todos": todo_list
    })


# @todo_routes.put("/todo/{id}")
# async def update_todo(id: int, new_todo: str):
#     todo_list[id] = new_todo
#     return {"message": "Todo updated successfully"}

# @todo_routes.put("/todo/{todo_id}")
# # update todo element
# async def update_todo(todo_id: int, item: TodoItem) -> dict:
#     for todo in todo_list:
#         if todo.id == todo_id:
#             todo.item = item.item
#             return {"message": f"Element {todo_id} updated correctly"}
#     return {"message": f"Element with ID {todo_id} doesnt exist"}


# @todo_routes.delete("/todo")
# delete element based on index
# async def delete_todo(todo: int):
#     for index in range(len(todo_list)):


@todo_routes.delete("/todo")
# delete all elements
async def delete_all_todos():
    if not todo_list:
        return {"message": "Todo list is empty"}
    else:
        todo_list.clear()
        return {"message": "List deleted succesfully"}
