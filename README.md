# Recipe Management Service

## Overview
This project is a basic recipe management service built with Flask. Recipes are stored in a local JSON file.

## Features
- Add, view, update, and delete recipes.
- Store recipe data persistently in a JSON file.

## Requirements
- Python 3.9+
- Flask

## Setup
1. Clone the repository to your local machine.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install Flask:
   ```bash
   pip install flask
   ```

4. Run the service:
   ```bash
   python web-service\app.py
   ```

5. Access the service at `http://127.0.0.1:5000/recipes`.

## API Endpoints
- `POST /recipes` - Add a new recipe.
- `GET /recipes` - Get all recipes.
- `GET /recipes/<id>` - Get a specific recipe.
- `PUT /recipes/<id>` - Update a recipe.
- `DELETE /recipes/<id>` - Delete a recipe.