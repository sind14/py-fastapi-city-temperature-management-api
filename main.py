from fastapi import FastAPI
from settings import Base, engine
from city.router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="City Temperature Management API")

app.include_router(router)
