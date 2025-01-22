from fastapi import FastAPI
from app.routes import hello, add, fakestore

app = FastAPI()

# Include the routers
app.include_router(hello.router)
app.include_router(add.router)
app.include_router(fakestore.router)

# FastAPI will auto-generate routes from `app/routes/hello.py`, `add.py`, and `fakestore.py`
