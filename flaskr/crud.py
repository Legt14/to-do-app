from .fb_config import db

def get_user(user_id):
    
    return db.collection('user').document(user_id).get()


def get_user_tasks(user_id):
    doc_ref = db.collection('user').document(user_id).collection('tasks')
    doc = doc_ref.stream()
    tasks = [record.to_dict() for record in doc]
    
    return tasks


def task_creator(user_id, data):

    return db.collection('user').document(user_id).collection('tasks').document().set(data)


def get_emial(email):
    
    return db.collection('user').document(email).get()


def user_register(user_id, data):

     return db.collection('user').document(user_id).set(data)

