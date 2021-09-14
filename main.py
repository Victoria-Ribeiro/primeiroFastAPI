from typing import List, Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Film(BaseModel):
    movie_id: str
    rating: int = Query(..., gt=0, lt=5)
    commentaries: str


@app.post("/films/", response_model=Film)
async def create_films(films: Film):
    return films
