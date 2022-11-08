from .fb_config import db

def get_users():
    doc_ref = db.collection('user')
    doc = doc_ref.stream()
    return doc


def get_user_tasks(user_id):
    doc_ref = db.collection('user').document(user_id).collection('tasks')
    doc = doc_ref.stream()
    for record in doc:
        a = record.to_dict()
    return a['title']