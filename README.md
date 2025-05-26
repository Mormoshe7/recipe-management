# Succeeded push to main branch
# Recipe Management Service

## Overview
This project is a basic recipe management service built with Flask. Recipes are stored in a Redis.

## Features
- Add, view, update, and delete recipes.
- Store recipe data persistently in Redis (or JSON for development).

## Requirements
- Python 3.9+
- Flask
- Redis (for production)

 ## Prerequisites

Before you can run the project, ensure that both Git and Docker are installed on your machine.
Installing Git:

If Git is not installed on your machine, run the following command in PowerShell as Administrator:

      winget install --id Git.Git -e --source winget

After installation, verify that Git is installed by running:

    git --version

    This should display the installed version of Git.

Installing Docker:

To install Docker Desktop, run the following command in PowerShell as Administrator:

      winget install --id Docker.DockerDesktop -e --source winget

After installation, restart your computer to ensure Docker is properly set up.

Once the computer restarts, make sure Docker is running by checking for the Docker whale icon in the taskbar. You can also verify Docker installation by running:

      docker --version
      docker compose version

## Setup
Open Command Prompt (CMD) from the project's folder:

- Navigate to the project folder in File Explorer.

- In the address bar at the top of the window, type cmd and press Enter. This will open Command Prompt directly in the project directory.

1.Clone the repository to your local machine:
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
   pip install -r web-service/requirements.txt
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
- `POST /recipes` - Add a new recipe. - what the endpoint accept as body?
- `GET /recipes` - Get all recipes.
- `GET /recipes/<id>` - Get a specific recipe.
- `PUT /recipes/<id>` - Update a recipe. - what the endpoint accept as body?
- `DELETE /recipes/<id>` - Delete a recipe.
