import os
from fastapi import FastAPI
from models.models import *
from schemas.todo_schema import *
from mangum import Mangum


stage = os.environ.get('STAGE', None)
root_path = f"/{stage}" if stage else "/"


app = FastAPI(title="Todo-service")
# root_path=root_path


'''list all the todos'''
@app.get("/")
def list_todos():
    try:
        # get all todos
        all_todos = TodoModel.query("TODO")


        # A list to help format the todos when listed in the docs
        the_todos = []
        for t in all_todos:
            todo = {
                "id": t.id,
                "title": t.title,
                "status": t.status,
                "notes": t.notes
            }
            the_todos.append(todo)


        # if there are no todos
        if len(the_todos) <  1:
            the_todos = "No tasks in the todo table."


        # response
        response = {
            "status": 200,
            "message": f"Retrieving all todos",
            "list": the_todos
        }


        # return the response
        return response
    except:

        # if an error occurs
        response = {
            "status": 404,
            "message": "Error"
        }
        # return vague error messgae
        return response


'''create a new todo'''
@app.post("/")
def create_todo(request: TodoIn):
    try:
        request = request.dict()

        # add new todo to dynamoDB
        todo = TodoModel(
            title=request.get("title"),
            notes=request.get("notes"),
            status=request.get("status")
        )
        todo.save()

        # return status code, creation message, and data that was saved
        return {
            "status": 200,
            "message": "New task created",
            "task": TodoIn(
                title=todo.title,
                notes=todo.notes,
                status=todo.status
            )
        }
    except:

        # if an error occurs
        response = {
            "status": 404,
            "message": "Error, task not found"
        }
        # return vague error message
        return response


'''get a todo by id'''
@app.get("/{id}")
def get_todo(id: str):
    try:
        # query for todo
        todo = TodoModel.get("TODO", id)
        todo_show = {
            "id": todo.id,
            "title": todo.title,
            "status": todo.status,
            "notes": todo.notes
        }
        response = {
            "status": 200,
            "message": f"Task {todo.id} found",
            "Task": todo_show
        }
        return response
    except:
        response = {
            "status": 404,
            "message": "Todo not found"
        }
        return response


handler = Mangum(app)
