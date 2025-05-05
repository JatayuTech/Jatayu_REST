from fastapi import FastAPI
from database import database  # from your database.py
from routes import book_routes  # import your route/controller module

app = FastAPI(title="Library Management System")

# Connect to the database at startup
@app.on_event("startup")
async def startup():
    await database.connect()

# Disconnect from the database at shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(book_routes.router, prefix="/books", tags=["Books"])
