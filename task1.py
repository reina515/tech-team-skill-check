
#uvicorn which is the server that will run the fastapi application
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
api=FastAPI()#creating an api app
app = FastAPI()

#GET(get info),POST(create somthing in the server),PUT(change something to the servver),DELETE
##creating a to do list app

@api.get("/") #defining a path for the http get method
def read():
    return { "Hello AGC tech team!!"}

@api.get("/{name}")
def welcome_name(name: str):
    return {"message": f"Welcome, {name}!"}


tasks = []  
id_counter = 1 #gives unique ids to the tasts

class Task(BaseModel): # defines a pydantic model for a task
    title: str
    completed: bool = False

@app.post("/tasks")
def add_task(item: Task):
    global id_counter
    task = item.dict()# converts the pydantic object into a regular python dictionary
    task["id"] = id_counter
    tasks.append(task)
    id_counter += 1
    return task

@app.get("/tasks") #showing the tasks as they get updated 
def get_tasks():
    return tasks

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)  
            return {"message": "Task deleted", "task": task}
    raise HTTPException(status_code=404, detail="Task not found")
