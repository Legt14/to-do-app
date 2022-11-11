from .fb_config import db

def get_user(user_id):
    
    return db.collection('user').document(user_id).get()


def get_user_tasks(user_id):
    doc_ref = db.collection('user').document(user_id).collection('tasks')
    #ref = db.collection('user').document(user_id).collection('tasks').get()
    doc = doc_ref.stream()
    
    return doc


def task_creator(user_id, data):

    return db.collection('user').document(user_id).collection('tasks').document().set(data)


def put_task(user_id, task_id, data):

    return db.collection('user').document(user_id).collection('tasks').document(task_id).set(data)


def del_task(user_id, task_id):
    doc_ref = db.collection('user').document(user_id).collection("tasks").document(task_id)
    doc_ref.delete()


def get_emial(email):
    
    return db.collection('user').document(email).get()


def user_register(user_id, data):

     return db.collection('user').document(user_id).set(data)

