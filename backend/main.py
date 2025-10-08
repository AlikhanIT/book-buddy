from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from typing import List
from book_database import init_db, search_books
from nlp_processor import process_query, generate_response

app = FastAPI()

# CORS для связи с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BookRequest(BaseModel):
    query: str
    style: str  # "detailed" or "brief"

class BookResponse(BaseModel):
    title: str
    author: str
    genre: str
    description: str

@app.on_event("startup")
async def startup_event():
    init_db()

@app.post("/recommend", response_model=List[BookResponse])
async def recommend_books(request: BookRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    # Обработка запроса и поиск книг
    keywords = process_query(request.query)
    books = search_books(keywords)
    
    if not books:
        raise HTTPException(status_code=404, detail="No books found for the query")
    
    # Генерация ответа в зависимости от стиля
    response = []
    for book in books:
        description = generate_response(book, request.style)
        response.append(BookResponse(
            title=book["title"],
            author=book["author"],
            genre=book["genre"],
            description=description
        ))
    
    return response
