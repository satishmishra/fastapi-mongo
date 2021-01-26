from fastapi import FastAPI
from crud.server.routes.alerts import router as AlertRouter

app = FastAPI()

app.include_router(AlertRouter, tags=["Alert"], prefix="/alert")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this crud app!"}
