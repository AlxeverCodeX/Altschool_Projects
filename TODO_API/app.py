from apiflask import APIFlask, abort
from db import session, Task
from flask import jsonify
from  schemas import TaskOutputSchema, TaskCreateSchema, TaskUpdateSchema, DeleteAllTasksSchema

app = APIFlask(__name__)

@app.get("/")
def index():
    return {"message": "Hello World"}
 


"""
    get/task get_all_task
    post/task create_task
    get/task/<task_id> get_task_by_id
    put/task/<task_id> update_task
    delete/task/<task_id> delete_task
"""

@app.get("/tasks")
def get_all_task():
    posts = session.query(Task).all()

    schema = TaskOutputSchema()
    result = schema.dump(posts, many=True)
    return jsonify(result)


@app.post("/tasks")
@app.input(TaskCreateSchema)
@app.output(TaskOutputSchema)
def create_task(data):
    content = data.get("content")

    new_task = Task(content=content)

    session.add(new_task)
    session.commit()

    return new_task, 201


@app.get("/task/<int:task_id>")
@app.output(TaskOutputSchema)
def get_task_id(task_id):
    task = session.query(Task).filter_by(id=task_id).first()

    if task is not None: #empty
        return task, 200

    abort(404)



@app.put("/task/<int:task_id>")
@app.input(TaskUpdateSchema)
@app.output(TaskOutputSchema)
def update_task(task_id, data):
    content = data.get("content")
    is_completed = data.get('is_completed')

    task_to_update = session.query(Task).filter_by(id=task_id).first()

    task_to_update.is_completed = is_completed
    task_to_update.content = content
    
    session.commit()
    return task_to_update




@app.delete("/task/<int:task_id>")
def delete_task(task_id):
    task_to_delete = session.query(Task).filter_by(id=task_id).first()

    session.delete(task_to_delete)

    session.commit()

    return {"message": "Deleted"}, 204



@app.delete("/tasks")
@app.input(DeleteAllTasksSchema)
def delete_all_tasks(deleted_tasks):
    deleted_tasks = session.query(Task).delete()
    session.commit()
    return "", 204











    
 
