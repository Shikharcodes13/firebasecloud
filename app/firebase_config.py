import firebase_admin
from firebase_admin import credentials, db

def initialize_firebase():
    cred = credentials.Certificate("shikhar-bf3c8-firebase-adminsdk-fbsvc-99036133bd.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://shikhar-bf3c8-default-rtdb.firebaseio.com/"
    })
    return db
