import sqlite3
import csv
import os

def init_db():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    
    # Создание таблицы
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)
    
    # Проверка, заполнена ли база
    cursor.execute("SELECT COUNT(*) FROM books")
    if cursor.fetchone()[0] == 0:
        # Загрузка данных из CSV
        with open("books.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cursor.execute(
                    "INSERT INTO books (title, author, genre, description) VALUES (?, ?, ?, ?)",
                    (row["title"], row["author"], row["genre"], row["description"])
                )
    
    conn.commit()
    conn.close()

def search_books(keywords: list) -> list:
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    
    query = """
        SELECT title, author, genre, description
        FROM books
        WHERE genre LIKE ? OR author LIKE ? OR title LIKE ?
    """
    search_term = f"%{keywords[0]}%" if keywords else "%"
    cursor.execute(query, (search_term, search_term, search_term))
    books = [
        {"title": row[0], "author": row[1], "genre": row[2], "description": row[3]}
        for row in cursor.fetchall()
    ]
    
    conn.close()
    return books[:5]  # Ограничение до 5 книг
