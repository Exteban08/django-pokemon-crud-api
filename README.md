# Django Pokemon CRUD API

A Django REST API for managing Pokemon data with full CRUD operations.

## Features

- Fetch Pokemon data from an external Pokemon API
- Store Pokemon data in a local database
- CRUD operations (Create, Read, Update, Delete)
- Calculate Pokemon scores based on their stats

## API Endpoints

### Pokemon Data Management
- `GET /api/pokemon/?name={name}` - Fetch Pokemon details from the external API by name
- `POST /pokemon/` - Create a new Pokemon in the database
- `GET /pokemon/` - List all Pokemon in the database
- `GET /pokemon/{id}/` - Get Pokemon details from the database by ID
- `GET /pokemon/?name={name}` - Get Pokemon details from the database by name
- `PATCH /pokemon/{id}/` - Update Pokemon details (partial update)
- `DELETE /pokemon/{id}/` - Delete a Pokemon by ID

### Pokemon Score
- `GET /pokemon/{id}/score/` - Calculate and retrieve the score of a Pokemon by ID

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Exteban08/django-pokemon-crud-api.git
   cd django-pokemon-crud-api

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows:
   venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run migrations:
   ```bash
   python manage.py migrate

5. Start the development server:
   ```bash
   python manage.py runserver


### Technologies Used
- Python
- Django
- Django REST Framework
- External Pokemon API
