# TODO-API-using-fast-API
Building a Simple To-Do API with FastAPI and SQLite
Objective:
The goal of this assignment is to create a simple To-Do API using FastAPI, SQLAlchemy, and
SQLite. By completing this assignment, you'll learn how to set up a FastAPI project, create and use
database models, write CRUD operations, and test your API.
Fastapi Assignment
Part 1: Project Setup
1. Create a Project Directory:
 - Create a new directory for your project called `todo_api`.
 - Navigate into the directory.
2. Set Up a Virtual Environment:
 - Create a virtual environment using `python -m venv venv`.
 - Activate the virtual environment:
 - On Windows: `venv\Scripts\activate`
 - On macOS/Linux: `source venv/bin/activate`
3. Install Dependencies:
 - Install FastAPI, Uvicorn, SQLAlchemy, and SQLite:
 pip install fastapi uvicorn sqlalchemy
4. Create Project Structure:
 - Inside the `todo_api` directory, create the following structure:
 todo_api/
 ??? app/
 ? ??? __init__.py
 ? ??? main.py
 ? ??? models.py
 ? ??? schemas.py
 ? ??? crud.py
 ? ??? database.py
Fastapi Assignment
 ??? requirements.txt
Fastapi Assignment
Part 2: Database Configuration
1. Configure the Database:
 - In `app/database.py`, set up the SQLite database with SQLAlchemy.
Fastapi Assignment
Part 3: Define Models and Schemas
1. Define the To-Do Item Model:
 - In `app/models.py`, define the SQLAlchemy model for a to-do item.
2. Define Pydantic Schemas:
 - In `app/schemas.py`, define the Pydantic models.
Fastapi Assignment
Part 4: CRUD Operations
1. Create CRUD Operations:
 - In `app/crud.py`, define the CRUD operations.
Fastapi Assignment
Part 5: Create FastAPI Application
1. Create FastAPI Endpoints:
 - In `app/main.py`, create the FastAPI application and endpoints.
Fastapi Assignment
Part 6: Running and Testing the API
1. Run the Application:
 - Start the FastAPI application using Uvicorn:
 uvicorn app.main:app --reload
2. Test the API:
 - Navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.
 - Use the provided Swagger UI to test the following endpoints:
 - POST /items/ to create a new to-do item.
 - GET /items/{item_id} to retrieve a specific to-do item by ID.
 - GET /items/ to retrieve a list of to-do items.
 - PUT /items/{item_id} to update a to-do item by ID.
 - DELETE /items/{item_id} to delete a to-do item by ID.
Fastapi Assignment
Submission Requirements
1. Code Repository:
 - Create a public repository on GitHub and push your code.
 - Include a README.md file explaining how to set up and run the project.
2. Submit the Repository Link:
 - Submit the link to your GitHub repository
