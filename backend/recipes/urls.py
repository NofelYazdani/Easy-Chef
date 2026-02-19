from django.urls import path

from .views import CreateCommentView, CreateRecipeView, GetRecipeView, \
    LikeRecipeView, EditRecipeView, DeleteRecipeView, SearchRecipeView, FavouriteRecipeView, RateRecipeView

urlpatterns = [
    path('create/', CreateRecipeView.as_view()),
    path('details/<int:recipe_id>/', GetRecipeView.as_view()),
    path('create/comment/<int:recipe_id>/', CreateCommentView.as_view()),
    path('like/<int:recipe_id>/', LikeRecipeView.as_view()),
    path('edit/<int:id>/', EditRecipeView.as_view()),
    path('delete/<int:recipe_id>/', DeleteRecipeView.as_view()),
    path('search/', SearchRecipeView.as_view()),
    path('favourite/<int:recipe_id>/', FavouriteRecipeView.as_view()),
    path('rate/<int:recipe_id>/', RateRecipeView.as_view())
]
