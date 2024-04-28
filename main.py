from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database tables deleted")
    await create_tables()
    print("Database tables created")
    yield
    print("Shutting down")


app = FastAPI(lifespan=lifespan)


tasks = []


