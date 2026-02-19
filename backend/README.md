# 🍳 EasyChef

EasyChef is a full-stack recipe management web application that allows users to create, search, rate, and manage recipes with authentication, favourites, and shopping lists.

Built as part of CSC309 Phase 2 and designed using Django REST Framework with JWT authentication.

---

## 🚀 Features

### 👤 User Management
- Register using phone number authentication
- Login with JWT tokens
- View and edit profile
- Custom Django user model

### 🍲 Recipe Management
- Create recipes with:
  - Cuisine type
  - Multiple diets
  - Ingredients
  - Instructions
- Edit and delete recipes
- View recipe details

### ❤️ Social Features
- Like / Unlike recipes
- Comment on recipes
- Favourite recipes
- Rate recipes (1–5 stars)

### 🛒 Shopping List
- Add recipes to shopping list
- View combined ingredient totals

### 🔍 Search
- Filter recipes by:
  - Title
  - Cuisine
  - Diet
  - Ingredient
  - Owner name
  - Prep time

---

## 🛠 Tech Stack

- **Backend:** Django + Django REST Framework
- **Authentication:** JWT Tokens
- **Database:** SQLite / PostgreSQL
- **API Testing:** Postman
- **Languages:** Python

---

## 📂 API Endpoints

### Accounts

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/accounts/login/` | POST | Login user |
| `/accounts/register/` | POST | Register new user |
| `/accounts/profile/` | GET | Get logged-in user info |
| `/accounts/edit-profile/<pk>/` | PUT | Update profile |

Example: login requires phone + password in form-data. :contentReference[oaicite:0]{index=0}

---

### Recipes

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/recipes/create/` | POST | Create recipe |
| `/recipes/details/<id>/` | GET | Recipe details |
| `/recipes/edit/<id>/` | PUT | Edit recipe |
| `/recipes/delete/<id>/` | DELETE | Delete recipe |
| `/recipes/search/` | GET | Search recipes |
| `/recipes/create/comment/<id>/` | POST | Comment |
| `/recipes/like/<id>/` | POST | Like/Unlike |
| `/recipes/favourite/<id>/` | POST | Favourite |
| `/recipes/rate/<id>/` | POST | Rate recipe |

These endpoints allow full CRUD operations and user interaction with recipes. :contentReference[oaicite:1]{index=1}

---

### Shopping List

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/recipes/add-to-shopping-list/<id>/` | POST | Add recipe ingredients |
| `/recipes/get-shopping-list/` | GET | View shopping list |

The shopping list aggregates ingredients from selected recipes. :contentReference[oaicite:2]{index=2}

---

## 🧠 Database Models

### Custom User Model
- Phone number authentication
- Avatar image support
- Extends Django `AbstractUser`

Uses phone as the username field for authentication. :contentReference[oaicite:3]{index=3}

---

### Recipe Model Includes
- Title
- Description
- Cuisine
- Image
- Prep time
- Servings
- Owner

Additional models:
- Diet
- Ingredient
- Instruction
- Comment
- Like
- Favourite
- ShoppingList
- Rate :contentReference[oaicite:4]{index=4}

---

## 🧪 Example Workflow

1. Register account
2. Login and get JWT token
3. Create recipe
4. Add comments or likes
5. Favourite recipes
6. Add to shopping list
7. Search recipes by filters

---

## 🖥 How to Run Locally

```bash
git clone https://github.com/NofelYazdani/Easy-Chef.git
cd Easy-Chef
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
