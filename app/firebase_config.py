import firebase_admin
from firebase_admin import credentials, db

def initialize_firebase():
    cred = credentials.Certificate("path/to/your/credentials.json")    #Add your credentials.json file path here
    firebase_admin.initialize_app(cred, {
        "databaseURL": ""    #Remove the url because github didn't allow me to add it
    })
    return db
