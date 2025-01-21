from src.config.database import tasks_collection


def get_tasks():
    tasks = list(tasks_collection.find())
    return {"data":[{**task,"_id":str(task["_id"])} for task in tasks]}
