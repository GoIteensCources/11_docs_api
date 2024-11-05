from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import RedirectResponse

import uvicorn

from schemas import Movie, ListMovie

app = FastAPI(
    title="Project Home work #8",
    description="## author of this api is Olexandr",
    version="0.1b",
    docs_url="/docs",
    redoc_url="/api/documentation"
)


@app.get("/", include_in_schema=False)
async def docs():
    return RedirectResponse("/docs")


movie_db = [
    Movie(id=1, title="Inception", director="Christopher Nolan", release_year=2010, rating=8.8),
    Movie(id=2, title="The Matrix", director="Wachowski Sisters", release_year=1999, rating=8.7),
    Movie(id=3, title="Interstellar", director="Christopher Nolan", release_year=2014, rating=8.6)
]


@app.get("/movies", response_model=ListMovie, tags=["movie"])
async def get_movie():
    return ListMovie(movies=movie_db, count_movies=len(movie_db))


@app.post("/movies", response_model=Movie, summary="For create new movie", tags=["movie"])
async def create_movie(movie: Movie = Body(...,
                                           description="input model",
                                           example=Movie(id=4,
                                                           title="Ne some",
                                                           director="Some",
                                                           release_year=2023,
                                                           rating=9.5)
                                           )):
    """
    # This api fo create **movie**,
    # return created movie
    """
    if movie.id not in movie_db:
        movie_db.append(movie)
        return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.get("/movies/{id}", response_model=Movie)
async def get_movie_by_id(id: int):
    for movie in movie_db:
        if movie.id == id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.delete("/movies/{id}", response_model=Movie)
async def get_movie_by_id(id: int):
    for movie in movie_db:
        if movie.id == id:
            movie_db.remove(movie)
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
