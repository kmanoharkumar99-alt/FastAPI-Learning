from fastapi import FastAPI
from sqlmodel import SQLModel,Field,create_engine,Session,select
from pydantic import BaseModel 
from enum import Enum
from datetime import datetime
from fastapi import HTTPException


app=FastAPI()

class Task(SQLModel,table=True):
    id:int | None=Field(primary_key=True)
    title:str
    completed:bool=False

sqlite_file="task.db"
sqlite_url=f"sqlite:/// {sqlite_file}"

engine=create_engine(sqlite_url,echo=True)

SQLModel.metadata.create_all(engine)

@app.post("/tasks")
def create_task_in_DB(task:Task):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)

        return task

@app.get("/tasks")
def get_task(task:Task):
    with Session(engine) as session:
        tasks=session.exec(select(Task)).all()
        return tasks
    



# tasks=[]
# task_id=1

# class Task(BaseModel):
#     title:str
#     description:str
#     status:Taskstatus



# class Taskstatus(str,Enum):
#     pending="pending"
#     in_progress="in progress"
#     completed="completed"

# @app.post("/tasks")
# def create_task(task:Task):
#     global task_id
#     current_id=task_id
#     task_id+=1
    
#     new_task={
#         "task_id":current_id,
#         "task":task.title,
#         "decription":task.description,
#         "status":task.status,
#         "created_at":datetime.now()
#     }
#     tasks.append(new_task)
#     return tasks

# @app.get("/tasks/{task_id}")
# def get_task(task_id:int):
#     for task in tasks:
#         if task["task_id"]==task_id:
#             return task

#     raise HTTPException(status_code=404,detail="Task Not Found")

# @app.put("/tasks/{task_id}")
# def update_task(task_id:int,task:Task):
#     for existing_task in tasks:
#         if existing_task["task_id"]==task_id:
#             existing_task["task"]=task.title
#             existing_task["description"]=task.description
#             existing_task["status"]=task.status

#             return task

#     raise HTTPException(status_code=404,detail="task not found")


# @app.delete("/tasks/{task_id}")
# def delete_task(task_id:int,task:Task):
#     for existing_task in tasks:
#         if existing_task["task_id"]==task_id:
#             tasks.remove(existing_task)
#             return "task deleted succesfully"
        
#     raise HTTPException(status_code=404,detail="task not found")














