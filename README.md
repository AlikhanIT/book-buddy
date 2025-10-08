# BookBuddy

A book recommendation chatbot built with FastAPI, React, and DistilGPT-2.

## Prerequisites
- Docker
- Docker Compose

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/AlikhanIT/book-buddy/tree/main
   cd bookbuddy
   ```
2. Build and run the containers:
   ```bash
   docker-compose up --build
   ```
3. Access the application:
   - Frontend: `http://localhost:3000`
   - Backend API: `http://localhost:8000`

## Usage
- Enter a query (e.g., "fantasy book") in the input field.
- Select response style (brief or detailed).
- View recommended books displayed as cards.
