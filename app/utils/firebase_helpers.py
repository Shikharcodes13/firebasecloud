# app/utils/firebase_helpers.py
import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firebase():
    cred = credentials.Certificate("shikhar-bf3c8-firebase-adminsdk-fbsvc-99036133bd.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

def get_user_data(user_id: str):
    db = initialize_firebase()
    user_ref = db.collection("users").document(user_id)
    return user_ref.get().to_dict()
