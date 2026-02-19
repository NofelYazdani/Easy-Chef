from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

CUISINE_CHOICES = (
    ('Mexican', 'Mexican'),
    ('Italian', 'Italian'),
    ('Greek', 'Greek'),
    ('Spanish', 'Spanish'),
    ('Indian', 'Indian'),
    ('American', 'American'),
    ('Somalian', 'Somalian'),
    ('Algerian', 'Algerian'),
    ('Turkish', 'Turkish'),
    ('Japanese', 'Japanese'),
    ('Chinese', 'Chinese'),
    ('Vietnamese', 'Vietnamese')
)

DIET_CHOICES = (
    ('Halal', 'Halal'),
    ('Kosher', 'Kosher'),
    ('Vegan', 'Vegan'),
    ('Vegetarian', 'Vegetarian'),
    ('Gluten-Free', 'Gluten-Free'),
    ('Dairy-Free', 'Dairy-Free'),
    ('Keto', 'Keto'),
    ('Carnivore', 'Carnivore'),
    ('Pescatarian', 'Pescatarian')
)

class Recipe(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    cuisine = models.CharField(max_length=255, choices=CUISINE_CHOICES, default='Choose a cuisine')
    image = models.ImageField(upload_to='uploads/recipe_pictures/', blank=True)
    prep_time = models.CharField(max_length=255)
    servings = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Diet(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='diet', on_delete=models.CASCADE)
    diet = models.CharField(choices=DIET_CHOICES, max_length=255, default='Choose a diet')


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='instruction', on_delete=models.CASCADE)
    instruction = models.CharField(max_length=255)
    num = models.IntegerField()

class UploadedIngredient(models.Model):
    name = models.CharField(max_length=255)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredient')
    ingredient = models.ForeignKey(UploadedIngredient, on_delete=models.CASCADE)
    grams = models.IntegerField()


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comment')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, auto_created=True)
    comment = models.CharField(max_length=255)


class Like(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='like')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Favourite(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favourite')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


class ShoppingList(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='shopping_list')


class Rate(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='rating')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    rating = models.IntegerField()

