from transformers import pipeline
import re

# Инициализация модели
generator = pipeline("text-generation", model="distilgpt2")

def process_query(query: str) -> list:
    # Простое извлечение ключевых слов
    query = query.lower()
    keywords = re.findall(r'\w+', query)
    return [kw for kw in keywords if kw not in ["хочу", "книга", "про"]]

def generate_response(book: dict, style: str) -> str:
    if style == "brief":
        return f"{book['title']} by {book['author']} ({book['genre']})"
    else:
        prompt = f"Recommend the book '{book['title']}' by {book['author']} in the {book['genre']} genre."
        response = generator(prompt, max_length=50, num_return_sequences=1)[0]["generated_text"]
        return response.strip()
