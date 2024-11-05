from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int = Field(description="id ", title="Id for movie")
    title: str = Field(description="id ", title="Name of the movie")
    director: str
    release_year: int = Field(ge=1800, le=2024)
    rating: float = Field(ge=1, le=10)


class ListMovie(BaseModel):
    movies: list[Movie]
    count_movies: int
