from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import GetProfileView, RegisterView, EditProfileView, ShoppingListView, GetShoppingListView, MyRecipesView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', GetProfileView.as_view()),
    path('register/', RegisterView.as_view()),
    path('edit-profile/<int:pk>/', EditProfileView.as_view()),
    path('add-to-shopping-list/<int:recipe_id>/', ShoppingListView.as_view()),
    path('get-shopping-list/', GetShoppingListView.as_view()),
    path('my-recipes/', MyRecipesView.as_view())
]
