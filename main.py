from fastapi import FastAPI

app=FastAPI()

@app.get("/health")
def health():
    return{"status":"healthy"}

tasks=["play games","complete homework"]
@app.get("/tasks")
def task():
    return tasks

@app.post("/tasks")
def create_task(task:str):
    tasks.append(task)
    return task


