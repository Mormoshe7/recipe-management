# Recipe Management Service

## Overview
This project is a basic recipe management service built with Flask. Recipes are stored in a local JSON file or Redis (depending on configuration).

## Features
- Add, view, update, and delete recipes.
- Store recipe data persistently in Redis (or JSON for development).

## Requirements
- Python 3.9+
- Flask
- Redis (for production)

## Setup
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Mormoshe7/recipe-management.git
   cd recipe-management
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the service:
   ```bash
   python web-service\app.py
   ```

5. Access the service at `http://127.0.0.1:5000/recipes`.

## Running with Docker
1. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

2. Access the service at `http://127.0.0.1:5000`.

## API Endpoints
- `POST /recipes` - Add a new recipe.
- `GET /recipes` - Get all recipes.
- `GET /recipes/<id>` - Get a specific recipe.
- `PUT /recipes/<id>` - Update a recipe.
- `DELETE /recipes/<id>` - Delete a recipe.