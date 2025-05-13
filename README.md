# Django Pokemon CRUD API

A Django REST API for managing Pokemon data with full CRUD operations.

## Features

- Fetch Pokemon data from external Pokemon API
- Store Pokemon data in local database
- CRUD operations (Create, Read, Update, Delete)
- Calculate Pokemon scores based on their stats

## API Endpoints

- `GET /pokemon/{name}/` - Get Pokemon details from external API
- `POST /pokemon/` - Create a new Pokemon in the database
- `GET /pokemon/db/{name}/` - Get Pokemon details from the database
- `PUT /pokemon/{name}/` - Update Pokemon details
- `DELETE /pokemon/{name}/` - Delete a Pokemon
- `GET /pokemon/` - List all Pokemon in the database
- `GET /pokemon/scores/` - Get scores for all Pokemon

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/YOUR_USERNAME/django-pokemon-crud-api.git
   cd django-pokemon-crud-api
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Start the development server:
   ```
   python manage.py runserver
   ```

## Technologies Used

- Django
- Django REST Framework
- External Pokemon API
