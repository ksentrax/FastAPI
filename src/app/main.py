from fastapi import FastAPI
from .api import organizations
from .db import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(organizations.router,
                   prefix='/organizations',
                   tags=['organizations']
                   )
