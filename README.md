# Easy Chef

Easy Chef is a full-stack recipe-sharing web application built with **Django REST Framework** (backend) and **React** (frontend). It supports account-based authentication, recipe creation, social interactions (likes/comments/favourites/ratings), and a shopping-list workflow that aggregates ingredient quantities across saved recipes.

## Features

- **JWT authentication** with phone-number login.
- **Custom user profiles** with avatar uploads.
- **Recipe management**: create, view details, edit, delete.
- **Recipe metadata**: cuisine, prep time, servings, diets, ingredients, and step-by-step instructions.
- **Social actions**: like/unlike, favourite/unfavourite, comment, and 1–5 star rating.
- **Recipe search/discovery** with filtering and text search.
- **Shopping list support** with ingredient total aggregation across selected recipes.
- **My Recipes dashboard** endpoint for created, liked, favourited, commented, and rated recipes.

## Tech Stack

### Backend
- Python 3
- Django 4.1
- Django REST Framework
- Simple JWT (`djangorestframework-simplejwt`)
- `django-filter`
- `django-cors-headers`
- `django-phonenumber-field`
- SQLite (default)

### Frontend
- React 18 (Create React App)
- React Router v6
- Axios
- React Bootstrap + Bootstrap
- Font Awesome React

## Repository Structure

```text
Easy-Chef/
├── backend/
│   ├── accounts/           # User model, auth/profile/shopping-list endpoints
│   ├── recipes/            # Recipe/domain models and recipe APIs
│   ├── easychef/           # Django project settings and root URL config
│   ├── uploads/            # Media files (avatars, recipe images)
│   ├── requirements.txt
│   └── manage.py
├── frontend/
│   ├── src/
│   │   ├── home/
│   │   ├── login/
│   │   ├── signup/
│   │   ├── my_recipes/
│   │   └── App.js
│   └── package.json
└── README.md
```

## Data Model (High-Level)

- **NewUser**: custom auth model using `phone` as `USERNAME_FIELD`, with optional avatar.
- **Recipe**: main recipe entity (title, description, cuisine, prep time, servings, owner).
- **Instruction**: ordered step list attached to a recipe.
- **UploadedIngredient** + **Ingredient**: normalized ingredient names and recipe-specific quantities (grams).
- **Diet**: one-to-many diet tags per recipe.
- **Comment**, **Like**, **Favourite**, **Rate**: social interactions per user/recipe.
- **ShoppingList**: recipes a user has added for shopping aggregation.

## API Overview

Base URL: `http://127.0.0.1:8000/`

### Accounts (`/accounts/`)

- `POST /accounts/register/` — register a user.
- `POST /accounts/login/` — obtain JWT access/refresh token pair.
- `GET /accounts/profile/` — authenticated profile data.
- `PATCH /accounts/edit-profile/<pk>/` — update profile (owner only).
- `POST /accounts/add-to-shopping-list/<recipe_id>/` — toggle recipe in shopping list.
- `GET /accounts/get-shopping-list/` — aggregated shopping list totals.
- `GET /accounts/my-recipes/` — grouped list of user interactions.

### Recipes (`/recipes/`)

- `POST /recipes/create/` — create a recipe (with nested ingredients/instructions/diets payload).
- `GET /recipes/details/<recipe_id>/` — full recipe detail including derived like count + average rating.
- `POST /recipes/create/comment/<recipe_id>/` — add comment.
- `POST /recipes/like/<recipe_id>/` — toggle like.
- `POST /recipes/favourite/<recipe_id>/` — toggle favourite.
- `POST /recipes/rate/<recipe_id>/` — create/update rating (1–5).
- `PATCH /recipes/edit/<id>/` — edit recipe (owner only).
- `DELETE /recipes/delete/<recipe_id>/` — delete recipe (owner only).
- `GET /recipes/search/` — search + filter recipes.
  - Search fields: `title`, `owner_name`
  - Filter fields: `diet`, `ingredient`, `cuisine`, `prep_time`

## Local Development Setup

## 1) Backend setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs at `http://127.0.0.1:8000`.

## 2) Frontend setup (new terminal)

```bash
cd frontend
npm install
npm start
```

Frontend runs at `http://127.0.0.1:3000`.

## Authentication Notes

- The backend uses JWT auth (`Authorization: Bearer <access_token>`).
- The current frontend stores `access` in `sessionStorage` under key `token`.
- CORS is enabled for all origins in development.

## Pagination, Search, and Filtering

- DRF global pagination is configured with `LimitOffsetPagination` and `PAGE_SIZE = 7`.
- Use query params such as `?limit=7&offset=0` on list/search endpoints.
- `recipes/search/` supports both text search and filter-based queries.

## Current Frontend Routes

Defined routes in `frontend/src/App.js`:

- `/` → My Recipes page
- `/login` → Login page
- `/home` → Landing/home page

> Note: A signup component exists (`frontend/src/signup`) but is currently not wired to a route in `App.js`.

## Test Commands

Backend:

```bash
cd backend
python manage.py test
```

Frontend:

```bash
cd frontend
npm test
```

## Included Project Assets

- A pre-populated SQLite database (`backend/db.sqlite3`)
- Uploaded media files in `backend/uploads/`
- Postman collection for backend API exploration: `backend/Easychef.postman_collection.json`

## Known Development Considerations

- This repository is configured for local/dev usage (e.g., `DEBUG=True`, open CORS).
- `ALLOWED_HOSTS` is empty and should be set before deployment.
- Secrets and JWT lifetimes should be production-hardened for deployment.

## License

No license file is currently included in this repository.
