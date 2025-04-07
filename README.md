# django-crud-product-review-api
# Product & Review CRUD API - Django REST Framework

## Features

- Create, Read, Update, Delete Products
- Add and manage Product Reviews
- DRF-based API endpoints
- Built-in Django admin panel

## Tech Stack

- Python
- Django
- Django REST Framework


## API Endpoints

| Method | Endpoint               | Description                  |
|--------|------------------------|------------------------------|
| GET    | /api/products/         | List all products            |
| POST   | /api/products/         | Create a new product         |
| GET    | /api/products/<id>/    | Retrieve a single product    |
| PUT    | /api/products/<id>/    | Update a product             |
| DELETE | /api/products/<id>/    | Delete a product             |
| POST   | /api/products/<id>/reviews/ | Add a review to a product |
