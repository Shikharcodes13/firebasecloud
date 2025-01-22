from fastapi import APIRouter
from app.firebase_config import initialize_firebase
import datetime

router = APIRouter()

db = initialize_firebase()

@router.post("/add")
async def add_data():
    ref = db.reference("NewsTok_test_collection")
    data = {
        "Day of Week": "Monday",
        "Day of Month": 22,
        "Month": "Jan",
        "Timestamp": datetime.datetime.now().isoformat(),
    }
    ref.push(data)
    return {"message": "Data added successfully"}
